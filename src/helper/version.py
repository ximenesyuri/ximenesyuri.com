import re
from sphinx.util import logging

logger = logging.getLogger(__name__)

FRONTMATTER_REGEX = re.compile(
    r"^(\s*---[\r\n]+[\s\S]+?[\r\n]+---[\r\n]+)"
)
VERSION_FIELD_REGEX = re.compile(r"^\s*version:\s*(.+?)\s*$", re.MULTILINE)

def _process_version(app, docname, source):
    content = source[0]

    front_match = FRONTMATTER_REGEX.match(content)
    if not front_match:
        logger.debug(f'No frontmatter found for {docname}, skipping version check.')
        return

    frontmatter_block = front_match.group(0)
    version_match = VERSION_FIELD_REGEX.search(frontmatter_block)
    if version_match:
        version_value = version_match.group(1).strip()
        version_string = f'<version>version: {version_value}</version>\n\n'
        end_frontmatter = front_match.end()
        rest_content = content[end_frontmatter:]
        new_content = content[:end_frontmatter] + version_string + rest_content
        source[0] = new_content
        logger.debug(f'Injected <version> tag with "{version_value}" into {docname}')
    else:
        logger.debug(f'No "version" field found in frontmatter for {docname}')

def setup(app):
    app.connect('source-read', _process_version)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
