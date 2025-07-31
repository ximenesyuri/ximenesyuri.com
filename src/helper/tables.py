from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util import logging
import re

logger = logging.getLogger(__name__)

def split_table_blocks(text):
    lines = [l.rstrip('\r') for l in text.strip().splitlines()]
    if len(lines) < 4:
        return None
    sep_indices = [i for i, l in enumerate(lines) if re.match(r'^[-=_]{4,}\s*$', l)]
    if len(sep_indices) < 2:
        return None
    header_line = lines[0]
    sep1 = sep_indices[0]
    sep2 = sep_indices[-1]
    content_lines = lines[sep1 + 1:sep2]
    caption_line = ""
    for l in lines[sep2+1:]:
        if l.strip():
            caption_line = l.strip()
            break
    return (header_line, content_lines, caption_line)

def detect_column_boundaries(header_line):
    matches = list(re.finditer(r'(?:^| {2,})(\S)', header_line))
    starts = [m.start(1) for m in matches]
    boundaries = []
    for i in range(len(starts) - 1):
        boundaries.append(starts[i+1])
    return boundaries, starts

def parse_txt_table_line(line, boundaries, starts):
    fields = []
    for i, b in enumerate(boundaries):
        fields.append(line[starts[i]:b].rstrip())
    fields.append(line[starts[-1]:].rstrip())
    return fields

class CaptionedTableDiv(nodes.Element):
    pass

def visit_captioned_table_div_html(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='captioned-table'))

def depart_captioned_table_div_html(self, node):
    self.body.append('</div>\n')

def find_label_for_literalblock(literal):
    if literal.get('names'):
        return literal['names'][0]
    if 'ids' in literal and literal['ids']:
        return literal['ids'][0]
    return None

class TxtTableToNodeTransform(SphinxTransform):
    default_priority = 700

    def apply(self):
        for literal in list(self.document.traverse(nodes.literal_block)):
            text = literal.astext()
            result = split_table_blocks(text)
            if not result:
                continue
            header_line, content_lines, caption_line = result

            label = literal['ids'][0] if 'ids' in literal and len(literal['ids']) > 0 else None

            content_lines = [l for l in content_lines if l.strip()]
            boundaries, starts = detect_column_boundaries(header_line)
            header_entries = parse_txt_table_line(header_line, boundaries, starts)
            num_columns = len(header_entries)

            table = nodes.table(classes=['custom-pre-table'])
            tgroup = nodes.tgroup(cols=num_columns)
            table += tgroup

            for _ in header_entries:
                tgroup += nodes.colspec(colwidth=1)

            thead = nodes.thead()
            tgroup += thead
            row = nodes.row()
            for h in header_entries:
                entry = nodes.entry()
                entry += nodes.paragraph(text=h.strip())
                row += entry
            thead += row

            tbody = nodes.tbody()
            tgroup += tbody

            for line in content_lines:
                fields = parse_txt_table_line(line, boundaries, starts)
                fields = (fields + [""] * num_columns)[:num_columns]
                row = nodes.row()
                for f in fields:
                    entry = nodes.entry()
                    entry += nodes.paragraph(text=f.strip())
                    row += entry
                tbody += row

            wrapper = CaptionedTableDiv()
            wrapper += table

            if caption_line:
                ref_uri = f"#{label}" if label else "#"
                caption_para = nodes.paragraph()
                caption_ref = nodes.reference('', caption_line, refuri=ref_uri, classes=['table-caption'])
                caption_para += caption_ref
                wrapper += caption_para

            literal.replace_self(wrapper)

def setup(app):
    app.add_node(
        CaptionedTableDiv,
        html=(visit_captioned_table_div_html, depart_captioned_table_div_html)
    )
    app.add_transform(TxtTableToNodeTransform)
    logger.info("[txt-table] Extension enabled: converting txt literal tables to real tables at doctree stage")
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

