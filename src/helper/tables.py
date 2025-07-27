from docutils import nodes
from sphinx.transforms import SphinxTransform
from sphinx.util import logging
import re

logger = logging.getLogger(__name__)

table_pattern = re.compile(
    r'^(?P<header_line>.*?)\n'
    r'--+\n'
    r'(?P<content>.*?)\n'
    r'--+\n'
    r'(?P<caption>.*?)\s*$',
    re.DOTALL | re.MULTILINE
)

def parse_line(line, column_boundaries):
    entries = []
    current_pos = 0
    for boundary_pos in column_boundaries:
        entry = line[current_pos:boundary_pos].strip()
        entries.append(entry)
        current_pos = boundary_pos
    entries.append(line[current_pos:].strip())
    return entries

def get_boundaries(header_line):
    header_line = header_line.replace('\t', '    ')
    boundaries = []
    for match in re.finditer(r' {2,}', header_line):
        gap_start, gap_end = match.span()
        if gap_start > 0 and not header_line[gap_start-1].isspace():
            if gap_end < len(header_line):
                if not header_line[gap_end].isspace():
                    boundaries.append(gap_end)
    return sorted(list(set(boundaries)))

class TxtTableToNodeTransform(SphinxTransform):
    default_priority = 700

    def apply(self):
        for literal in self.document.traverse(nodes.literal_block):
            text = literal.astext()
            match = table_pattern.match(text.strip())
            if match:
                logger.info(f"[txt-table] Converting literal block to table in {self.env.docname}")
                header_line = match.group('header_line').rstrip()
                content_lines = match.group('content').strip().split('\n')
                caption_text = match.group('caption').strip()
                column_boundaries = get_boundaries(header_line)
                header_entries = parse_line(header_line, column_boundaries)

                table = nodes.table(classes=['custom-pre-table'])
                tgroup = nodes.tgroup(cols=len(header_entries))
                table += tgroup

                for _ in header_entries:
                    tgroup += nodes.colspec(colwidth=1)

                if caption_text:
                    table += nodes.caption('', caption_text)

                thead = nodes.thead()
                tgroup += thead
                row = nodes.row()
                for h in header_entries:
                    entry = nodes.entry()
                    entry += nodes.paragraph(text=h)
                    row += entry
                thead += row

                tbody = nodes.tbody()
                tgroup += tbody
                for line in content_lines:
                    row = nodes.row()
                    body_entries = parse_line(line.rstrip(), column_boundaries)
                    for i in range(len(header_entries)):
                        entry = nodes.entry()
                        text = body_entries[i] if i < len(body_entries) else ""
                        entry += nodes.paragraph(text=text)
                        row += entry
                    tbody += row

                literal.replace_self(table)

def setup(app):
    app.add_transform(TxtTableToNodeTransform)
    logger.info("[txt-table] Extension enabled: converting txt literal tables to real tables at doctree stage")
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
