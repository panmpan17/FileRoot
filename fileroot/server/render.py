import os
import cherrypy
import jinja2


__all__ = ["IndexHandler"]


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
        hidden_dirs = []

        path = os.path.join(os.getcwd(), *args)
        path = path.replace("...", "..")

        for blob in os.listdir(path):
            full_blob = os.path.join(path, blob)

            if os.path.isfile(full_blob):
                if blob.startswith("."):
                    hidden_files.append(blob)
                else:
                    files.append(blob)
            else:
                if full_blob.startswith("."):
                    hidden_dirs.append(blob)
                else:
                    dirs.append(blob)

        return self.render("tree.html", files=files, dirs=dirs,
                           hidden_files=hidden_files, hidden_dirs=hidden_dirs)
