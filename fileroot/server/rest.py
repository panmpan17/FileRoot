import os
import cherrypy


__all__ = ["TreeView"]


class View(object):
    _cp_config = {
        "tools.json_out.on": True,
        "tools.json_in.on": True,
        "tools.encode.on": True,
        "tools.encode.encodeing": "utf-8",
    }


class TreeView(View):
    _path = "tree/"

    @cherrypy.expose
    def index(self, rel_path=[]):
        if isinstance(rel_path, str):
            rel_path = [rel_path]

        path = os.path.abspath(os.path.join(os.getcwd(), *rel_path))
        rel_path = os.path.relpath(path, os.getcwd())

        files = []
        dirs = []
        hidden_files = []
        hidden_dirs = []

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

        return dict(path=path, rel_path=rel_path, files=files, dirs=dirs,
                    hidden_files=hidden_files, hidden_dirs=hidden_dirs)

    @cherrypy.expose
    def file(self):
        pass
