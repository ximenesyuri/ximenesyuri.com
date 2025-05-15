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

html_favicon = 'static/favicon.svg'
html_show_sphinx = False
html_link_suffix = ''

html_context={
    'title': 'Yuri Ximenes',
    'menu': {
        'home': '/',
        'about': '/about',
        'education': '/education',
        'development': '/development',
        'research': '/research',
        'publications': '/publications',
        'work': '/work',
        'setup': '/setup'
    }
}

html_sidebars = {
  "**": [
      "sidebar.html",
      "sidebar_toc.html"
    ]
}
