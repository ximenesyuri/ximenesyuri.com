import os
import re
import io
import yaml
from pathlib import Path
from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)

class title_placeholder(nodes.General, nodes.Element):
    pass

class TitleDirective(SphinxDirective):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        return [title_placeholder()]

def parse_frontmatter(filepath):
    if not os.path.exists(filepath):
        return {}
    with io.open(filepath, 'r', encoding='utf8') as f:
        content = f.read()
    fm = {}
    if content.startswith('---'):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if m:
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except Exception as e:
                logger.warning(f"[inject-md-title] Could not parse YAML frontmatter in {filepath}: {e}")
    return fm or {}

def get_file_desc(app, docname):
    """
    For current doc: safely parse the source Markdown frontmatter.
    1. 'desc'
    2. 'title'
    3. filename (no .md)
    """
    filepath = app.env.doc2path(docname)
    fm = parse_frontmatter(filepath)
    if "desc" in fm and fm["desc"]:
        return str(fm["desc"])
    elif "title" in fm and fm["title"]:
        return str(fm["title"])
    else:
        return Path(filepath).stem

def get_doc_h1(app, docname):
    try:
        title_node = app.env.titles.get(docname, None)
        if title_node:
            return title_node.astext().strip()
    except Exception:
        pass
    return ""

def get_frontmatter_from_env(app, docname):
    if hasattr(app.env, "metadata"):
        return app.env.metadata.get(docname, {}) or {}
    return {}

def get_index_name(app, current_docname):
    srcdir = Path(app.srcdir).resolve()
    doc_path = Path(app.env.doc2path(current_docname)).resolve()
    idx_path = (doc_path.parent / "index.md").resolve()
    try:
        rel_index_path = idx_path.relative_to(srcdir)
        index_docname = str(rel_index_path).replace("\\", "/")[:-3]
    except Exception:
        return idx_path.parent.name

    meta = get_frontmatter_from_env(app, index_docname)
    name = None
    if "title" in meta and meta["title"]:
        name = meta["title"]
    if not name:
        h1 = get_doc_h1(app, index_docname)
        if h1:
            name = h1
    if not name:
        name = idx_path.parent.name
    return str(name or "Index")

class TitleTransform(SphinxTransform):
    default_priority = 100
    def apply(self):
        app = self.env.app
        docname = self.env.docname
        for node in self.document.traverse(title_placeholder):
            index_name = get_index_name(app, docname)
            file_desc = get_file_desc(app, docname)
            htmlblock = (
                f'<div class="title">\n'
                f'<h0>{index_name}</h0>\n'
                f'<s0>{file_desc}</s0>\n'
                f'</div>\n'
            )
            raw_html = nodes.raw('', htmlblock, format='html')
            node.replace_self(raw_html)
            logger.info(f"[inject-md-title] Injected into {docname}: index_name={index_name} file_desc={file_desc}")

def setup(app):
    app.add_directive('title', TitleDirective)
    app.add_transform(TitleTransform)
    try:
        from myst_parser.extensions.sphinx import registry as myst_registry
        myst_registry.directives["title"] = TitleDirective
    except Exception:
        pass
    logger.info("inject-md-title: Extension loaded.")
    return {"parallel_read_safe": True, "parallel_write_safe": True}
