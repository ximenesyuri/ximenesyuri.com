import re
import os

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

def _get_markdown_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines_read = 0
            for line in f:
                lines_read += 1
                match = re.match(r'^\s*#\s*(.+)', line)
                if match:
                    return match.group(1).strip()
                if line.strip() == '' or lines_read > 20:
                    break
    except Exception as e:
        print(f"Warning: Could not read title from {filepath}: {e}")
    return None

def _build_menu_from_fs(current_fs_path, content_root_path, content_prefix_for_urls=''):
    menu_node = []

    items = sorted(os.listdir(current_fs_path))
    dirs = [item for item in items if os.path.isdir(os.path.join(current_fs_path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(current_fs_path, item)) and item.endswith('.md')]

    for dname in dirs:
        dir_full_path = os.path.join(current_fs_path, dname)
        dir_url_segment = os.path.join(content_prefix_for_urls, dname).replace(os.sep, '/')

        dir_display_title = dname.replace('_', ' ')
        dir_index_path = os.path.join(dir_full_path, 'index.md')
        if os.path.exists(dir_index_path):
            dir_index_title = _get_markdown_title(dir_index_path)
            if dir_index_title:
                dir_display_title = dir_index_title
            dir_link = dir_url_segment + '/index'
        else:
            dir_link = None
        dir_node = {
            'title': dir_display_title,
            'is_dir': True,
            'link': dir_link,
            'children': _build_menu_from_fs(dir_full_path, content_root_path, dir_url_segment)
        }
        menu_node.append(dir_node)

    for fname in files:
        if fname == 'index.md':
            continue

        file_full_path = os.path.join(current_fs_path, fname)
        basename = os.path.splitext(fname)[0]
        title = _get_markdown_title(file_full_path)
        file_url_segment = os.path.join(content_prefix_for_urls, basename).replace(os.sep, '/')

        menu_node.append({
            'link': file_url_segment,
            'title': title if title else basename.replace('_', ' '),
            'is_dir': False
        })

    return menu_node

def _get_libs_menu_items(base_content_dir):
    libs_content_path = os.path.join(base_content_dir, 'libs')

    if not os.path.exists(libs_content_path):
        return []

    final_menu = []

    libs_index_path = os.path.join(libs_content_path, 'index.md')
    libs_index_title = _get_markdown_title(libs_index_path) 

    final_menu.extend(_build_menu_from_fs(libs_content_path, base_content_dir, 'libs'))
    return final_menu

conf_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(conf_dir, '..'))
BASE_CONTENT_DIR = os.path.join(project_root, 'content')

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
        'libs': '/libs/index' # This is a global menu item, keep as is
    },
    'libs_side_menu': _get_libs_menu_items(BASE_CONTENT_DIR)
}


html_sidebars = {
    "**": [
        "sidebar_toc.html" # Table of contents for the current page
    ],
    'libs/*': [
        "sidebar.html"
    ]
}

myst_enable_includes = True
