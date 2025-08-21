import os
import sys
import yaml
from src.helper.menu import _get_menu_items
from src.helper.date import _year, _now
sys.path.insert(0, os.path.abspath('./helper'))

extensions = [
    'myst_parser',
    'toc',
    'tables',
    'autolink',
    'draft',
    'version'
]

source_suffix = ['.md']
master_doc = 'index'

templates_path = ['templates']
exclude_patterns = []

suppress_warnings = [
    'toc.not_included',
    'app.add_node',
]

html_title = 'yx'
html_static_path = ['static', '../assets']
html_permalinks_icon = ""
myst_number_code_blocks = ["python"]
highlight_language = None

html_favicon = '/_static/favicon.svg'
html_show_sphinx = False
html_link_suffix = ''
html_use_dirhtml = True

myst_enable_includes = True

CONF_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(CONF_DIR, '..'))
CONTENT_DIR = os.path.join(ROOT_DIR, 'content')

html_context={
    'title': 'Yuri Ximenes',
    'year': _year(),
    'now': _now(),
    'menu': {
        'home': {"path": "/"},
        'about': {"path": '/about'},
        'education': {"path": '/education'},
        'research': {"path": '/research'},
        'publications': {"path": '/publications'},
        'work': {"path": '/work'},
        'setup': {"path": '/setup'},
        'libs': {"path": '/libs', "class": ""},
        'notes': {"path": '/notes', "class": ""}
    },
    'libs_menu': _get_menu_items(CONTENT_DIR, 'libs'),
    'notes_menu': _get_menu_items(CONTENT_DIR, 'notes')
}

autolink = {
    "global": {},
    "l": {
        "class": "autolink-libs"
    },
    "n": {
        "class": "autolink-notes"
    },
    "g": {
        "class": "autolink-glossary"
    },
    "p": {
        "class": "autolink-python"
    },

}

with open(os.path.join(CONF_DIR, 'yml', 'global.yml'), 'r') as file:
    autolink["global"]["entries"] = yaml.safe_load(file)

with open(os.path.join(CONF_DIR, 'yml', 'libs.yml'), 'r') as file:
    autolink["l"]["entries"] = yaml.safe_load(file)

with open(os.path.join(CONF_DIR, 'yml', 'notes.yml'), 'r') as file:
    autolink["n"]["entries"] = yaml.safe_load(file)

with open(os.path.join(CONF_DIR, 'yml', 'glossary.yml'), 'r') as file:
    autolink["g"]["entries"] = yaml.safe_load(file)

with open(os.path.join(CONF_DIR, 'yml', 'python.yml'), 'r') as file:
    autolink["p"]["entries"] = yaml.safe_load(file)
