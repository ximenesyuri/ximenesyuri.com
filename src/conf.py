import sys
from utils import yml, path
from src.helper.menu import _get_menu_items
from src.helper.date import _year, _now
path.insert('./helper')

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

CONF_DIR = path.dirname(__file__)
YML_DIR = path.join(CONF_DIR, "yml")
ROOT_DIR = path.join(CONF_DIR, '..')
CONTENT_DIR = path.join(ROOT_DIR, 'content')

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
    "global": {
        "class": "autolink-global",
        "entries": yml.read(path.join(YML_DIR, "global.yml"))
    },
    "lib": {
        "class": "autolink-libs",
        "entries": yml.read(path.join(YML_DIR, "libs/libs.yml"))
    },
    "notes": {
        "class": "autolink-notes",
        "entries": yml.read(path.join(YML_DIR, "notes.yml"))
    },
    "general": {
        "class": "autolink-glossary-general",
        "entries": yml.read(path.join(YML_DIR, "glossary/general.yml"))
    },
    "logic": {
        "class": "autolink-glossary-logic",
        "entries": yml.read(path.join(YML_DIR, "glossary/logic.yml"))
    },
    "py": {
        "class": "autolink-python",
        "entries": yml.read(path.join(YML_DIR, "python.yml"))
    },

}

libs = ["comp", "typed"]

for lib in libs:
    lib_yml = path.join(YML_DIR, f"libs/{lib}.yml")
    autolink['lib']['entries'].update(yml.read(lib_yml))
