import re
from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)

def is_inside_reference(node):
    parent = getattr(node, 'parent', None)
    while parent is not None:
        if isinstance(parent, nodes.reference):
            return True
        parent = getattr(parent, 'parent', None)
    return False

def get_delimiters(autolink_config):
    delimiters = [("{", "}")]
    if "__delimiters__" in autolink_config:
        delimiters = autolink_config["__delimiters__"]
    delims = []
    for item in delimiters:
        if isinstance(item, (tuple, list)) and len(item) == 2:
            delims.append((str(item[0]), str(item[1])))
    return delims

def build_delimiter_regex(delimiters):
    regex_list = []
    for left, right in delimiters:
        l = re.escape(left)
        r = re.escape(right)
        regex = rf"{l}(?:([\w\-_]+)\s*:\s*([^\{{\}}]+?)|([^\{{\}}]+?)){r}"
        regex_list.append(regex)
    pattern = "|".join(regex_list)
    return re.compile(pattern)

def _collect_terms(autolinks):
    sources = {}
    global_terms = {}
    source_classes = {}

    for source, source_data in autolinks.items():
        if source == "__delimiters__":
            continue
        if not isinstance(source_data, dict):
            continue
        entries = source_data.get("entries", {})
        s_classes = source_data.get("classes") or source_data.get("class") or []
        if isinstance(s_classes, str):
            s_classes = s_classes.split()
        source_classes[source] = list(s_classes)
        if source == "global":
            for entry_key, entry in entries.items():
                for term in entry.get("terms", []):
                    global_terms[term.lower()] = (entry_key, entry)
        else:
            if source not in sources:
                sources[source] = {}
            if entries:
                for entry_key, entry in entries.items():
                    for term in entry.get("terms", []):
                        sources[source][term.lower()] = (entry_key, entry)
    return sources, global_terms, source_classes

class AutoLinkPostTransform(SphinxPostTransform):
    default_priority = 900
    def run(self):
        autolink_config = self.app.config.autolink
        if not autolink_config:
            logger.warning("autolink extension: 'autolink' not defined in conf.py.")
            return

        delimiters = get_delimiters(autolink_config)
        term_pattern = build_delimiter_regex(delimiters)

        sources, global_terms, source_classes = _collect_terms(autolink_config)

        for text_node in list(self.document.traverse(nodes.Text)):
            parent = text_node.parent
            if parent is None:
                continue
            if is_inside_reference(text_node):
                continue

            text = text_node.astext()
            matches = list(term_pattern.finditer(text))
            if not matches:
                continue

            new_nodes = []
            last_idx = 0

            for match in matches:
                matched_full = match.group(0)
                prefix = match.group(1)
                body = match.group(2)
                global_body = match.group(3)

                if match.start() > last_idx:
                    new_nodes.append(nodes.Text(text[last_idx:match.start()]))

                classes = []
                url = None
                entry_label = None

                if prefix and body:
                    source = prefix.strip()
                    entry_term = body.strip()
                    term_l = entry_term.lower()
                    source_map = sources.get(source)
                    if source_map and term_l in source_map:
                        entry_key, entry = source_map[term_l]
                        url = entry.get("url")
                        entry_label = entry_term
                        classes = ["autolink"]
                        classes += source_classes.get(source, [])
                        if entry.get("classes") or entry.get("class"):
                            ec = entry.get("classes") or entry.get("class")
                            if isinstance(ec, str): ec = ec.split()
                            classes += list(ec)
                    else:
                        new_nodes.append(nodes.Text(matched_full))
                        last_idx = match.end()
                        continue

                elif global_body:
                    entry_term = global_body.strip()
                    term_l = entry_term.lower()
                    if term_l in global_terms:
                        entry_key, entry = global_terms[term_l]
                        url = entry.get("url")
                        entry_label = entry_term
                        classes = ["autolink"]
                        classes += source_classes.get("global", [])
                        if entry.get("classes") or entry.get("class"):
                            ec = entry.get("classes") or entry.get("class")
                            if isinstance(ec, str): ec = ec.split()
                            classes += list(ec)
                    else:
                        new_nodes.append(nodes.Text(matched_full))
                        last_idx = match.end()
                        continue

                if url and entry_label:
                    ref_attribs = {'refuri': url, 'classes': classes}
                    style = entry.get("style")
                    if style:
                        ref_attribs["style"] = style
                    ref_node = nodes.reference(**ref_attribs)
                    ref_node += nodes.Text(entry_label)
                    new_nodes.append(ref_node)
                else:
                    new_nodes.append(nodes.Text(matched_full))

                last_idx = match.end()

            if last_idx < len(text):
                new_nodes.append(nodes.Text(text[last_idx:]))
            idx = parent.index(text_node)
            parent.children[idx:idx+1] = new_nodes
            for node in new_nodes:
                node.parent = parent

def setup(app):
    app.add_config_value('autolink', {}, 'env')
    app.add_post_transform(AutoLinkPostTransform)
    return {
        'version': '0.7',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

