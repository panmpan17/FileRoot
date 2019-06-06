import os
import cherrypy
import jinja2


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))


class Handler(object):
    def render(self, src, **kwargs):
        return jinja_env.get_template(src).render(kwargs)


class IndexHandler(Handler):
    _path = "/"

    @cherrypy.expose
    def index(self):
        return self.render("index.html")

    @cherrypy.expose
    def tree(self, *args, **kwargs):
        files = []
        dirs = []
        hidden_files = []
        hideen_dirs = []

        for blob in os.listdir(os.path.join(os.getcwd(), *args)):
            if os.path.isfile(blob):
                if blob.startswith("."):
                    hidden_files.append(blob)
                else:
                    files.append(blob)
            else:
                if blob.startswith("."):
                    hideen_dirs.append(blob)
                else:
                    dirs.append(blob)

        return self.render("tree.html", files=files, dirs=dirs,
                           hidden_files=hidden_files, hideen_dirs=hideen_dirs)
