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
        left_esc = re.escape(left)
        right_esc = re.escape(right)
        regex_list.append(f"{left_esc}(.*?){right_esc}")
    pattern = "|".join(regex_list)
    return re.compile(pattern)

class AutoLinkPostTransform(SphinxPostTransform):
    default_priority = 900
    def run(self):
        autolink_config = self.app.config.autolink
        if not autolink_config:
            logger.warning("autolink extension: 'autolink' not defined in conf.py.")
            return

        delimiters = get_delimiters(autolink_config)
        term_pattern = build_delimiter_regex(delimiters)

        term_to_entry_map = {}
        for entry_data in autolink_config.values():
            if not isinstance(entry_data, dict):
                continue
            if 'terms' in entry_data and 'url' in entry_data:
                for term in entry_data['terms']:
                    term_to_entry_map[term.lower()] = entry_data

        for text_node in list(self.document.traverse(nodes.Text)):
            parent = text_node.parent
            if parent is None:
                continue
            if not isinstance(parent, nodes.paragraph):
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
                # Find which group matched and extract
                matched_term_full = match.group(0)
                matched_term_content = None
                # Which group contains the match? (groups 1,3,5,...)
                for g in range(1, len(match.groups()) + 1):
                    content = match.group(g)
                    if content is not None:
                        matched_term_content = content.strip()
                        break

                if match.start() > last_idx:
                    new_nodes.append(nodes.Text(text[last_idx:match.start()]))

                entry_data = None
                if matched_term_content:
                    entry_data = term_to_entry_map.get(matched_term_content.lower())
                if entry_data:
                    ref_attribs = {'refuri': entry_data['url'], 'classes': ['autolink']}
                    classes = ref_attribs['classes'].copy()
                    custom_class = entry_data.get("class")
                    if custom_class:
                        if isinstance(custom_class, str):
                            classes += custom_class.split()
                        elif isinstance(custom_class, (list, tuple)):
                            classes += list(custom_class)
                        classes = [c for c in classes if c]
                        ref_attribs['classes'] = classes
                    style = entry_data.get("style")
                    if style:
                        ref_attribs["style"] = style

                    ref_node = nodes.reference(**ref_attribs)
                    ref_node += nodes.Text(matched_term_content)
                    new_nodes.append(ref_node)
                else:
                    new_nodes.append(nodes.Text(matched_term_full))
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
    app.add_css_file('autolink.css')  # optional
    return {
        'version': '0.6',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
