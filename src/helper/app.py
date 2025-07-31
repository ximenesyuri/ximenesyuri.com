from pygments.lexer import RegexLexer, bygroups, include, using, this, DelegatingLexer, Lexer
from pygments.token import *
from pygments.lexers.python import PythonLexer
from pygments.lexers.templates import 

class PythonWithJinjaLexer(RegexLexer):
    name = 'PythonWithJinja'
    aliases = ['python+jinja', 'py+jinja', 'pythonwithjinja']
    filenames = ['*.py']
    mimetypes = ['text/x-python']

    tokens = {
        'root': [
            # Start of a jinja block (with triple quotes + "jinja")
            (r'([urURfFbB]*)([\'\"]{3})jinja(\r?\n)', 
            bygroups(String.Affix, String.Double, Whitespace), 'jinja-block'),
            # Any other triple quoted string
            (r'([urURfFbB]*)([\'\"]{3})', bygroups(String.Affix, String.Double), 'python-string'),
            # Delegate the rest to the PythonLexer (line-by-line!)
            (r'[^\n\'"]+', using(PythonLexer)),
            (r'[\n\'"]', using(PythonLexer)),
        ],
        'jinja-block': [
            # End of the jinja triple quoted string
            (r'([\'\"]{3})', String.Double, '#pop'),
            # Jinja content: highlight with the html+django lexer (jinja2)
            (r'[^\'"]+', using(HtmlDjangoLexer)),
            (r'[\n\'"]', using(HtmlDjangoLexer)),
        ],
        'python-string': [
            (r'([\'\"]{3})', String.Double, '#pop'),
            (r'.|\n', String.Double),
        ],
    }


def setup(app):
    from pygments.lexers import get_lexer_by_name
    app.add_lexer('python+jinja', PythonWithJinjaLexer)
    app.add_lexer('py+jinja', PythonWithJinjaLexer)
    app.add_lexer('pythonwithjinja', PythonWithJinjaLexer)
