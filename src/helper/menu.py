import os
import re
import yaml

def _get_markdown_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        yaml_match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
        if yaml_match:
            frontmatter_str = yaml_match.group(1)
            try:
                frontmatter = yaml.safe_load(frontmatter_str)
                if isinstance(frontmatter, dict) and 'title' in frontmatter:
                    return str(frontmatter['title']).strip()
            except yaml.YAMLError as e:
                print(f"Warning: Could not parse YAML frontmatter in {filepath}: {e}")
            markdown_content = yaml_match.group(2)
        else:
            markdown_content = content

        lines_read = 0
        for line in markdown_content.splitlines():
            lines_read += 1
            h1_match = re.match(r'^\s*#+\s*(.+)', line)
            if h1_match:
                return h1_match.group(1).strip()
            if line.strip() == '' or lines_read > 20:
                break

    except Exception as e:
        print(f"Warning: Could not read title from {filepath}: {e}")
    return None

def _is_draft(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(2048)
        yaml_match = re.match(r'---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if yaml_match:
            frontmatter = yaml.safe_load(yaml_match.group(1))
            if isinstance(frontmatter, dict) and frontmatter.get('draft', False):
                return True
    except Exception:
        pass
    return False

def _build_menu_from_fs(current_fs_path, content_root_path, rel_url_prefix=''):
    menu_node = []
    items = sorted(os.listdir(current_fs_path))
    dirs = [item for item in items if os.path.isdir(os.path.join(current_fs_path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(current_fs_path, item)) and item.endswith('.md')]

    for dname in dirs:
        dir_full_path = os.path.join(current_fs_path, dname)
        dir_index_path = os.path.join(dir_full_path, 'index.md')
        rel_path_from_root = os.path.relpath(dir_full_path, content_root_path)
        rel_path_slug = rel_path_from_root.replace(os.sep, '/')
        dir_title = dname.replace('_', ' ')
        dir_link = None
        if os.path.exists(dir_index_path) and not _is_draft(dir_index_path):
            index_title = _get_markdown_title(dir_index_path)
            if index_title:
                dir_title = index_title
            dir_link = rel_path_slug
        children = _build_menu_from_fs(dir_full_path, content_root_path)
        menu_node.append({
            'title': dir_title,
            'is_dir': True,
            'link': dir_link,
            'children': children
        })

    for fname in files:
        if fname == 'index.md':
            continue
        file_full_path = os.path.join(current_fs_path, fname)
        if _is_draft(file_full_path):
            continue
        basename = os.path.splitext(fname)[0]
        rel_path_from_root = os.path.relpath(file_full_path, content_root_path)
        rel_path_slug = rel_path_from_root.replace(os.sep, '/')
        rel_path_slug = re.sub(r'\.md$', '', rel_path_slug)
        menu_node.append({
            'link': rel_path_slug,
            'title': _get_markdown_title(file_full_path) or basename.replace('_', ' '),
            'is_dir': False
        })

    return menu_node

def _get_menu_items(content_dir, inner_path):
    content_path = os.path.join(content_dir, inner_path)
    if not os.path.exists(content_path):
        return []
    return _build_menu_from_fs(content_path, content_dir)

