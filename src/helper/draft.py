import os
import re
import yaml
from sphinx.util import logging

logger = logging.getLogger(__name__)

DRAFT_DOCNAMES = set()

def setup(app):
    app.connect('source-read', filter_draft_doc)
    return {'version': '1.0', 'parallel_read_safe': True}

def parse_frontmatter(src):
    m = re.match(r'^---\s*\n(.*?\n?)^---\s*(?:\n|$)', src, re.DOTALL | re.MULTILINE)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except Exception:
        return None

def filter_draft_doc(app, docname, source):
    srcdir = app.srcdir
    for ext in ('.md', '.rst'):
        fname = os.path.join(srcdir, docname.replace("/", os.sep) + ext)
        if not os.path.isfile(fname):
            continue
        with open(fname, encoding="utf-8") as f:
            meta = parse_frontmatter(f.read(2048))
        if isinstance(meta, dict) and meta.get("draft", False):
            logger.info(f"[draft] Excluding doc: {docname} (marked as draft in frontmatter)")
            source[0] = ""  # Provide an empty docstring
            DRAFT_DOCNAMES.add(docname)
            break
