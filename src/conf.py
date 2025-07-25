import os

from src.helper.menu import _get_menu_items

extensions = [
    'myst_parser'
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
html_static_path = ['static']
html_permalinks_icon = ""
myst_number_code_blocks = ["python"]
highlight_language = None

html_favicon = 'static/favicon.svg'
html_show_sphinx = False
html_link_suffix = ''
html_use_dirhtml = True

myst_enable_includes = True

conf_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(conf_dir, '..'))
CONTENT_DIR = os.path.join(project_root, 'content')

html_context={
    'title': 'Yuri Ximenes',
    'menu': {
        'home': '/',
        'about': '/about',
        'education': '/education',
        'research': '/research',
        'publications': '/publications',
        'work': '/work',
        'setup': '/setup',
        'libs': '/libs',
        'notes': '/notes'
    },
    'libs_menu': _get_menu_items(CONTENT_DIR, 'libs')
}
