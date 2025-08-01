import os
import re
import yaml

def _parse_frontmatter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(4096)
        m = re.match(r'^---\s*\n(.*?)(?:\n)?---\s*\n', content, re.DOTALL)
        if m:
            frontmatter = yaml.safe_load(m.group(1)) or {}
            rest = content[m.end():]
            return frontmatter, rest
    except Exception as e:
        print(f"Warning: Could not parse frontmatter in {filepath}: {e}")
    return {}, None

def _get_markdown_title(filepath):
    frontmatter, markdown_content = _parse_frontmatter(filepath)
    if isinstance(frontmatter, dict) and 'title' in frontmatter:
        return str(frontmatter['title']).strip()
    if not markdown_content:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        except Exception:
            return None
    for i, line in enumerate(markdown_content.splitlines()):
        if i > 20:
            break
        m = re.match(r'^\s*#+\s*(.+)', line)
        if m:
            return m.group(1).strip()
    return None

def _get_weight(filepath):
    frontmatter, _ = _parse_frontmatter(filepath)
    w = frontmatter.get('weight', None)
    try:
        return int(w) if w is not None else None
    except Exception:
        return None

def _is_draft(filepath):
    frontmatter, _ = _parse_frontmatter(filepath)
    return bool(frontmatter.get('draft', False)) if isinstance(frontmatter, dict) else False

def _sort_items(items):
    """Sort a list of menu entries by weight then title, return new list."""
    return sorted(
        items,
        key=lambda n: (
            n.get('weight') if n.get('weight') is not None else float('inf'),
            n['title'].lower()
        )
    )

def _slugify(name):
    return name.lower().replace(' ', '-')

def _build_menu_from_fs(current_fs_path, content_root_path):
    menu_dict = {}

    if not os.path.isdir(current_fs_path):
        return menu_dict

    items = os.listdir(current_fs_path)
    entries = []

    for name in items:
        full_path = os.path.join(current_fs_path, name)
        rel_path_from_root = os.path.relpath(full_path, content_root_path)
        rel_path_slug = rel_path_from_root.replace(os.sep, '/')

        # Directory
        if os.path.isdir(full_path):
            index_path = os.path.join(full_path, 'index.md')
            has_index = os.path.isfile(index_path) and not _is_draft(index_path)
            children = _build_menu_from_fs(full_path, content_root_path)
            # Directory node uses its index.md weight/title, or fallback
            if has_index:
                weight = _get_weight(index_path)
                title = _get_markdown_title(index_path) or name.replace('_', ' ')
                link = rel_path_slug
            else:
                weight = None
                title = name.replace('_', ' ')
                link = None
            if has_index or children:
                entries.append({
                    'slug': name,  # keep original dir name as key
                    'title': title,
                    'is_dir': True,
                    'link': link,
                    'children': children,
                    'weight': weight,
                })
        # File (not index.md)
        elif os.path.isfile(full_path) and name.endswith('.md') and name != 'index.md':
            if _is_draft(full_path):
                continue
            basename = os.path.splitext(name)[0]
            rel_path_md_slug = re.sub(r'\.md$', '', rel_path_slug)
            weight = _get_weight(full_path)
            title = _get_markdown_title(full_path) or basename.replace('_', ' ')
            entries.append({
                'slug': basename,
                'title': title,
                'is_dir': False,
                'link': rel_path_md_slug,
                'children': {},
                'weight': weight,
            })

    # Sort by weight, then title
    entries = _sort_items(entries)
    # Remove weight key and convert list to dict
    for item in entries:
        item.pop('weight', None)
        slug = item.pop('slug')
        menu_dict[slug] = item
    return menu_dict

def _get_menu_items(content_dir, inner_path):
    content_path = os.path.join(content_dir, inner_path)
    if not os.path.exists(content_path):
        return {}
    return _build_menu_from_fs(content_path, content_dir)

