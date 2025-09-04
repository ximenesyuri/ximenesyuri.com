import re
import os
from pathlib import Path
import yaml
from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)


def extract_frontmatter_weight(project_srcdir, docname, possible_suffixes):
    for suffix in possible_suffixes:
        candidate = Path(project_srcdir) / (docname + suffix)
        if candidate.is_file():
            with candidate.open("rt", encoding="utf-8") as f:
                text = f.read()
            if text.startswith('---'):
                block_end = text.find('---', 3)
                if block_end != -1:
                    block = text[3:block_end].strip()
                    match = re.search(r'^weight:\s*([\'"]?)([\d]+)\1$', block, re.MULTILINE)
                    if match:
                        try:
                            return int(match.group(2))
                        except Exception:
                            return None
    return None

def extract_frontmatter_draft(project_srcdir, docname, possible_suffixes):
    for suffix in possible_suffixes:
        candidate = Path(project_srcdir) / (docname + suffix)
        if candidate.is_file():
            with candidate.open("rt", encoding="utf-8") as f:
                text = f.read()
            if text.startswith('---'):
                block_end = text.find('---', 3)
                if block_end != -1:
                    block = text[3:block_end].strip()
                    try:
                        data = yaml.safe_load(block)
                        if isinstance(data, dict):
                            draft_val = data.get("draft")
                            if isinstance(draft_val, bool):
                                return draft_val
                            if isinstance(draft_val, str):
                                if draft_val.strip().lower() in ("true", "yes", "on", "1"):
                                    return True
                        return False
                    except Exception:
                        if re.search(r'^draft:\s*(true|True|yes|on|1)\s*$', block, re.MULTILINE):
                            return True
                        return False
    return False

def try_read_frontmatter_title(project_srcdir, docname, possible_suffixes):
    logger = logging.getLogger(__name__)
    for suffix in possible_suffixes:
        candidate = Path(project_srcdir) / (docname + suffix)
        if candidate.is_file():
            with candidate.open("rt", encoding="utf-8") as f:
                text = f.read()
            if text.startswith('---'):
                block_end = text.find('---', 3)
                if block_end != -1:
                    block = text[3:block_end].strip()
                    match = re.search(r'^title:\s*[\'"]?(.+?)[\'"]?$', block, re.MULTILINE)
                    if match:
                        title = match.group(1).strip()
                        return title
    return None

class toc_placeholder(nodes.General, nodes.Element):
    pass

class toc_hor_placeholder(nodes.General, nodes.Element):
    pass

class toc_dir_placeholder(nodes.General, nodes.Element):
    pass

class TocDirective(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        node = toc_placeholder()
        source, line = self.state_machine.get_source_and_line(self.lineno)
        node.source = source
        node.line = line
        return [node]

class TocHorDirective(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        node = toc_hor_placeholder()
        source, line = self.state_machine.get_source_and_line(self.lineno)
        node.source = source
        node.line = line
        return [node]

class TocDirDirective(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        return [toc_dir_placeholder()]

class TocTransform(SphinxTransform):
    default_priority = 100

    def apply(self):
        for node in self.document.traverse(toc_placeholder):
            self.process_page_toc(node)

    def process_page_toc(self, placeholder_node):
        toc_list_items = []
        placeholder_line = getattr(placeholder_node, 'line', None)

        section_nodes = list(self.document.traverse(nodes.section))
        if section_nodes:
            for section in section_nodes:
                title_node = section.next_node(nodes.title)
                if not title_node:
                    continue

                title_line = getattr(title_node, 'line', None)
                if placeholder_line is not None and title_line is not None:
                    if title_line < placeholder_line:
                        continue

                if (section.parent is self.document
                   and section is self.document.children[0]):
                    doc_title_node = self.env.titles.get(self.env.docname)
                    doc_title = (doc_title_node.astext().strip()
                                 if doc_title_node else "")
                    if title_node.astext().strip() == doc_title:
                        continue

                title_text = title_node.astext()
                section_id = section.get('ids', [None])[0]
                if not section_id:
                    continue

                li = nodes.list_item()
                p = nodes.paragraph()
                ref = nodes.reference('', '', internal=True, refid=section_id)
                ref += nodes.Text(title_text)
                p += ref
                li += p
                toc_list_items.append(li)
        else:
            for node in self.document.children:
                if isinstance(node, nodes.title):
                    title_line = getattr(node, 'line', None)
                    if placeholder_line is not None and title_line is not None:
                        if title_line < placeholder_line:
                            continue

                    doc_title_node = self.env.titles.get(self.env.docname)
                    doc_title = (doc_title_node.astext().strip() if doc_title_node else "")
                    if node.astext().strip() == doc_title:
                        continue

                    title_text = node.astext()
                    parent = node.parent
                    section_id = None
                    if parent and parent.get('ids'):
                        section_id = parent['ids'][0]
                    elif node.get('ids'):
                        section_id = node['ids'][0]
                    if not section_id:
                        continue

                    li = nodes.list_item()
                    p = nodes.paragraph()
                    ref = nodes.reference('', '', internal=True, refid=section_id)
                    ref += nodes.Text(title_text)
                    p += ref
                    li += p
                    toc_list_items.append(li)

        if toc_list_items:
            toc_container = nodes.enumerated_list()
            toc_container['enumtype'] = 'arabic'
            toc_container['prefix'] = ''
            toc_container['suffix'] = '.'
            for item in toc_list_items:
                toc_container += item
            placeholder_node.replace_self(toc_container)
        else:
            placeholder_node.replace_self(nodes.paragraph())

class TocHorTransform(SphinxTransform):
    default_priority = 100

    def apply(self):
        for node in self.document.traverse(toc_hor_placeholder):
            self.process_page_toc_hor(node)

    def process_page_toc_hor(self, placeholder_node):
        toc_links = []
        placeholder_line = getattr(placeholder_node, 'line', None)

        section_nodes = list(self.document.traverse(nodes.section))
        if section_nodes:
            for section in section_nodes:
                title_node = section.next_node(nodes.title)
                if not title_node:
                    continue

                title_line = getattr(title_node, 'line', None)
                if placeholder_line is not None and title_line is not None:
                    if title_line < placeholder_line:
                        continue

                if (section.parent is self.document
                   and section is self.document.children[0]):
                    doc_title_node = self.env.titles.get(self.env.docname)
                    doc_title = (doc_title_node.astext().strip()
                                 if doc_title_node else "")
                    if title_node.astext().strip() == doc_title:
                        continue

                title_text = title_node.astext()
                section_id = section.get('ids', [None])[0]
                if not section_id:
                    continue

                ref = nodes.reference('', '', internal=True, refid=section_id)
                ref += nodes.Text(title_text)
                toc_links.append(ref)
        else:
            for node in self.document.children:
                if isinstance(node, nodes.title):
                    title_line = getattr(node, 'line', None)
                    if placeholder_line is not None and title_line is not None:
                        if title_line < placeholder_line:
                            continue

                    doc_title_node = self.env.titles.get(self.env.docname)
                    doc_title = (doc_title_node.astext().strip() if doc_title_node else "")
                    if node.astext().strip() == doc_title:
                        continue

                    title_text = node.astext()
                    parent = node.parent
                    section_id = None
                    if parent and parent.get('ids'):
                        section_id = parent['ids'][0]
                    elif node.get('ids'):
                        section_id = node['ids'][0]
                    if not section_id:
                        continue

                    ref = nodes.reference('', '', internal=True, refid=section_id)
                    ref += nodes.Text(title_text)
                    toc_links.append(ref)

        if toc_links:
            para = nodes.paragraph()
            for idx, ref in enumerate(toc_links):
                para += ref
                if idx < len(toc_links) - 1:
                    para += nodes.Text(" | ")
            placeholder_node.replace_self(para)
        else:
            placeholder_node.replace_self(nodes.paragraph())

class TocDirTransform(SphinxTransform):
    default_priority = 100

    def apply(self):
        for node in self.document.traverse(toc_dir_placeholder):
            self.process_directory_toc(node)

    def process_directory_toc(self, placeholder_node):
        logger = logging.getLogger(__name__)

        docname = self.env.docname
        current_doc_path_source = Path(self.env.doc2path(docname))
        if not current_doc_path_source.is_absolute():
            current_doc_path_source = Path(self.app.srcdir) / current_doc_path_source
        current_dir_source = current_doc_path_source.parent

        toc_list_items = []
        all_docnames = sorted(self.env.found_docs)
        current_doc_output_path = Path(self.app.builder.get_outfilename(docname))

        sibling_docnames = []
        for other in all_docnames:
            p = Path(self.env.doc2path(other))
            if not p.is_absolute():
                p = Path(self.app.srcdir) / p
            if (p.parent == current_dir_source
               and other != docname
               and Path(other).stem != "index"):
                sibling_docnames.append(other)

        cfg = self.env.config
        if hasattr(cfg, "source_suffix"):
            if isinstance(cfg.source_suffix, dict):
                suffixes = list(cfg.source_suffix)
            elif isinstance(cfg.source_suffix, (list, tuple)):
                suffixes = list(cfg.source_suffix)
            elif isinstance(cfg.source_suffix, str):
                suffixes = [cfg.source_suffix]
            else:
                suffixes = [".md", ".rst"]
        else:
            suffixes = [".md", ".rst"]

        toc_entries = []
        for other in sibling_docnames:
            meta = self.env.metadata.get(other, {})
            is_draft = False
            if "draft" in meta:
                d = meta["draft"]
                if d is True or (isinstance(d, str) and d.strip().lower() in ("true", "yes", "on", "1")):
                    is_draft = True
            else:
                is_draft = extract_frontmatter_draft(self.app.srcdir, other, suffixes)
            if is_draft:
                continue

            weight = None
            if "weight" in meta:
                try:
                    weight = int(str(meta["weight"]))
                except Exception:
                    weight = None
            if weight is None:
                weight = extract_frontmatter_weight(self.app.srcdir, other, suffixes)

            link_text = meta.get("title")
            if not link_text:
                link_text = try_read_frontmatter_title(self.app.srcdir, other, suffixes)
            if not link_text:
                tn = self.env.titles.get(other)
                if tn:
                    txt = tn.astext().strip()
                    if txt and txt != "<no title>":
                        link_text = txt.replace("<no title>", "").strip()
            if not link_text:
                stem = Path(other).stem
                link_text = " ".join(w.capitalize() for w in stem.replace("-", " ").replace("_", " ").split())

            other_out = Path(self.app.builder.get_outfilename(other))
            try:
                rel = other_out.relative_to(current_doc_output_path.parent).as_posix()
            except Exception:
                logger.warning(
                    f"Could not compute relative URI between "
                    f"{current_doc_output_path} and {other_out}.",
                    type="toc_generator",
                )
                rel = other_out.name

            toc_entries.append({
                "docname": other,
                "weight": weight,
                "link_text": link_text,
                "relative_uri": rel,
            })

        ordered = sorted(
            toc_entries,
            key=lambda e: (
                e["weight"] is None,
                e["weight"] if e["weight"] is not None else 0,
                e["link_text"].lower(),
            ),
        )
        for entry in ordered:
            li = nodes.list_item()
            p = nodes.paragraph()
            ref = nodes.reference(
                "",
                "",
                internal=True,
                refuri=entry["relative_uri"],
                name=entry["link_text"],
            )
            ref += nodes.Text(entry["link_text"])
            p += ref
            li += p
            toc_list_items.append(li)
            logger.info(
                f"[toc-dir] Added '{entry['docname']}' "
                f"(text={entry['link_text']}, uri={entry['relative_uri']}, "
                f"weight={entry['weight']})"
            )

        if toc_list_items:
            toc_container = nodes.enumerated_list()
            toc_container["enumtype"] = "arabic"
            toc_container["prefix"] = ""
            toc_container["suffix"] = "."
            for li in toc_list_items:
                toc_container += li
            placeholder_node.replace_self(toc_container)
        else:
            placeholder_node.replace_self(nodes.paragraph())

def setup(app):
    app.add_directive('toc', TocDirective)
    app.add_directive('toc-hor', TocHorDirective)
    app.add_directive('toc-dir', TocDirDirective)
    app.add_transform(TocTransform)
    app.add_transform(TocHorTransform)
    app.add_transform(TocDirTransform)
    logger.info("Initialized toc_generator extension.")

    try:
        from myst_parser.extensions.sphinx import registry as myst_registry
        myst_registry.directives["toc"] = TocDirective
        myst_registry.directives["toc-hor"] = TocHorDirective
        myst_registry.directives["toc-dir"] = TocDirDirective
        logger.info("Registered TOC directives with myst-parser.")
    except ImportError:
        pass

    return {
        'version': '0.12',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

