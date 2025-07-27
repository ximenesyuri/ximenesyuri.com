import os
from pathlib import Path
from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)

class toc_placeholder(nodes.General, nodes.Element): pass
class toc_dir_placeholder(nodes.General, nodes.Element): pass

class TocDirective(SphinxDirective):
    has_content = False; required_arguments = 0; optional_arguments = 0; final_argument_whitespace = False
    def run(self): return [toc_placeholder()]
class TocDirDirective(SphinxDirective):
    has_content = False; required_arguments = 0; optional_arguments = 0; final_argument_whitespace = False
    def run(self): return [toc_dir_placeholder()]

class TocTransform(SphinxTransform):
    default_priority = 100

    def apply(self):
        for node in self.document.traverse(toc_placeholder):
            self.process_page_toc(node)

    def process_page_toc(self, placeholder_node):
        logger = logging.getLogger(__name__)
        toc_list_items = []
        section_nodes = list(self.document.traverse(nodes.section))

        if section_nodes:
            for section in section_nodes:
                if section.parent is self.document and section is self.document.children[0]:
                    title_node = section.next_node(nodes.title)
                    if title_node and hasattr(self.env, 'titles'):
                        doc_title = getattr(self.env.titles.get(self.env.docname, None), 'astext', lambda: "")()
                        if title_node.astext().strip() == doc_title:
                            continue
                title_node = section.next_node(nodes.title)
                if title_node:
                    title_text = title_node.astext()
                    section_id = section['ids'][0] if section['ids'] else None
                    if section_id:
                        list_item = nodes.list_item()
                        paragraph = nodes.paragraph()
                        reference = nodes.reference('', '', internal=True, refid=section_id, name=title_text)
                        reference += nodes.Text(title_text)
                        paragraph += reference
                        list_item += paragraph
                        toc_list_items.append(list_item)
        else:
            for node in self.document.children:
                if isinstance(node, nodes.title):
                    title_text = node.astext()
                    section_id = node.parent['ids'][0] if node.parent and 'ids' in node.parent and node.parent['ids'] else None
                    if not section_id and 'ids' in node:
                        section_id = node['ids'][0]
                    if hasattr(self.env, 'titles'):
                        doc_title = getattr(self.env.titles.get(self.env.docname, None), 'astext', lambda: "")()
                        if title_text.strip() == doc_title:
                            continue
                    if section_id:
                        list_item = nodes.list_item()
                        paragraph = nodes.paragraph()
                        reference = nodes.reference('', '', internal=True, refid=section_id, name=title_text)
                        reference += nodes.Text(title_text)
                        paragraph += reference
                        list_item += paragraph
                        toc_list_items.append(list_item)
        if toc_list_items:
            toc_container = nodes.enumerated_list()
            toc_container['enumtype'] = 'arabic'
            toc_container['prefix'] = ''
            toc_container['suffix'] = '.'
            for item in toc_list_items:
                toc_container += item
            placeholder_node.replace_self(toc_container)
            logger.info(f"Injected page TOC with {len(toc_list_items)} items into {self.env.docname}.")
        else:
            logger.info(f"No headings found to include in page TOC for {self.env.docname}.")
            placeholder_node.replace_self(nodes.paragraph())


class TocDirTransform(SphinxTransform):
    default_priority = 100
    def apply(self):
        for node in self.document.traverse(toc_dir_placeholder):
            self.process_directory_toc(node)
    def process_directory_toc(self, placeholder_node):
        docname = self.env.docname
        current_doc_path_source = Path(self.env.doc2path(docname))
        if not current_doc_path_source.is_absolute():
            current_doc_path_source = Path(self.app.srcdir) / current_doc_path_source
        current_dir_source = current_doc_path_source.parent
        toc_list_items = []
        all_docnames = sorted(self.env.found_docs)
        current_doc_output_path = Path(self.app.builder.get_outfilename(docname))
        for other_docname in all_docnames:
            other_doc_path_source = Path(self.env.doc2path(other_docname))
            if not other_doc_path_source.is_absolute():
                 other_doc_path_source = Path(self.app.srcdir) / other_doc_path_source
            if (other_doc_path_source.parent == current_dir_source and
                other_docname != docname and
                Path(other_docname).stem != 'index'):
                calculated_link_text = None
                metadata = self.env.metadata.get(other_docname, {})
                frontmatter_title = metadata.get('title')
                if frontmatter_title:
                    text = str(frontmatter_title).strip()
                    if text:
                        calculated_link_text = text
                        logger.debug(f"  - Using frontmatter title for '{other_docname}': '{calculated_link_text}'")
                if not calculated_link_text:
                    title_node = self.env.titles.get(other_docname)
                    if title_node:
                        text = title_node.astext().strip()
                        if text and text != "<no title>":
                            calculated_link_text = text.replace("<no title>", "").strip()
                            logger.debug(f"  - Using H1 (or main RST title) for '{other_docname}': '{calculated_link_text}'")
                        else:
                            logger.debug(f"  - H1/main title for '{other_docname}' found but was empty or lacked content ('{text}').")
                if not calculated_link_text:
                    calculated_link_text = ' '.join([word.capitalize() for word in Path(other_docname).stem.replace('-', ' ').replace('_', ' ').split()])
                    logger.debug(f"  - Using filename as fallback for '{other_docname}': '{calculated_link_text}'")
                link_text = calculated_link_text
                other_doc_output_path = Path(self.app.builder.get_outfilename(other_docname))
                try:
                    src_dir = current_doc_output_path.parent
                    target_path = other_doc_output_path
                    relative_uri = target_path.relative_to(src_dir).as_posix()
                except ValueError:
                    logger.warning(f"Could not determine relative path between {current_doc_output_path} and {other_doc_output_path}. Falling back.", type="toc_generator")
                    relative_uri = other_doc_output_path.name
                list_item = nodes.list_item(); paragraph = nodes.paragraph()
                reference = nodes.reference('', '', internal=True, refuri=relative_uri, name=link_text)
                reference += nodes.Text(link_text); paragraph += reference; list_item += paragraph
                toc_list_items.append(list_item)
                logger.debug(f"  - Added directory file: '{other_docname}' (Text: {link_text}, URI: {relative_uri})")
            else:
                 logger.debug(f"  - Skipping directory doc: {other_docname}. Conditions (parent same, not self, not index): {other_doc_path_source.parent == current_dir_source}, {other_docname != docname}, {Path(other_docname).stem != 'index'}")
        if toc_list_items:
            toc_container = nodes.enumerated_list(); toc_container['enumtype'] = 'arabic'; toc_container['prefix'] = ''; toc_container['suffix'] = '.'
            for item in toc_list_items: toc_container += item
            placeholder_node.replace_self(toc_container)
            logger.info(f"Injected directory TOC with {len(toc_list_items)} items into {self.env.docname}.")
        else:
            logger.info(f"No other files found in the directory for '{docname}' to add to TOC.")
            placeholder_node.replace_self(nodes.paragraph())

def setup(app):
    app.add_directive('toc', TocDirective)
    app.add_directive('toc-dir', TocDirDirective)
    app.add_transform(TocTransform)
    app.add_transform(TocDirTransform)
    logger.info("Initialized toc_generator extension with 'toc' and 'toc-dir' directives and custom placeholder nodes.")

    try:
        from myst_parser.extensions.sphinx import registry as myst_registry
        myst_registry.directives["toc"] = TocDirective
        myst_registry.directives["toc-dir"] = TocDirDirective
        logger.info("Registered 'toc' and 'toc-dir' with myst-parser for Markdown (.md)")
    except Exception:
        pass

    return {
        'version': '0.11',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
