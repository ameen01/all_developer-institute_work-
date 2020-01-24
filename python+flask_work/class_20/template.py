import jinja2

my_cv = "ameen.html"
outfile = 'rendered.html'
connten = open(my_cv, 'r').read()
class commenit:
    def __init__(self, tital):
        self.tital = tital


mylng = ["hebrow", "english", "arabic", "fur"]
template = jinja2.Template(connten)
rendered = template.render(pname= "ameen", lnag=mylng)

open(outfile, 'w').write(rendered)