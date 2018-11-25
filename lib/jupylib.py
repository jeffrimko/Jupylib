##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import uuid
from IPython.display import display, Javascript, HTML, Markdown

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def html(s):
    display(HTML(s))
def md(s):
    display(Markdown(s))
def h1(s):
    display(HTML("<h1>%s</h1>" % (s)))
def h2(s):
    display(HTML("<h2>%s</h2>" % (s)))
def h3(s):
    display(HTML("<h3>%s</h3>" % (s)))
def h4(s):
    display(HTML("<h4>%s</h4>" % (s)))
def h5(s):
    display(HTML("<h5>%s</h5>" % (s)))

def hide_code(hidden=True):
    """Function to hide the code cells in a notebook.

    **Attribution**:
    Based on code from `harshil <https://stackoverflow.com/a/28073228/789078>`_.
    """
    html("""\
            <script>
            code_show=%s;
            function code_toggle() {
                if (code_show){
                    $('div.input').hide();
                } else {
                    $('div.input').show();
                }
                code_show = !code_show
            }
            $(document).ready(code_toggle);
            </script>
            <form action="javascript:code_toggle()">
            <input type="submit" value="Toggle Code Cells">
            </form>""" % ("true" if hidden else "false"))

def show_toc():
    """Shows TOC for the document.

    **Attribution**:
    Uses and based on code from `kmahelona
    <https://github.com/kmahelona/ipython_notebook_goodies>`_.
    """
    html("""\
            <script>
            $.getScript('https://kmahelona.github.io/ipython_notebook_goodies/ipython_notebook_toc.js')
            </script>
            <h2 id="tocheading">Table Of Contents</h2>
            <div id="toc"></div><hr>""")

def json(data):
    """Displays JSON/dicts using a collapsible format.

    **Attribution**:
    Based on code from `slashvee
    <https://www.reddit.com/r/IPython/comments/34t4m7/lpt_print_json_in_collapsible_format_in_ipython/>`_.
    """
    if isinstance(data, dict):
        data = ujson.encode(data)
    uid = str(uuid.uuid4())
    display(HTML('<div id="{0}" style="height: 600px; width:100%;"></div>'.format(uid)))
    display(Javascript("""
    require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
      document.getElementById('%s').appendChild(renderjson(%s))
    });
    """ % (uid, data)))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass
