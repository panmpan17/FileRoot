import os
import cherrypy

from . import render
from . import rest


class Server:
    config = {
        "server.socket_host": "127.0.0.1",
        "server.socket_port": 8080,
        "server.thread_pool": 100,
        "server.max_request_body_size": 500000000,
        "server.socket_timeout": 5,

        # "server.ssl_certificate": "/path/to/some.crt",
        # "server.ssl_private_key": "/path/to/some.key",
        "tools.force_https.on": False,
    }

    static_config = {
        "/static": {
            "tools.staticdir.root": os.getcwd(),
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "static",
        }
    }

    @classmethod
    def parse_config(cls, config):
        cls.config["server.socket_host"] = config.host
        cls.config["server.socket_port"] = config.port
        cls.config["server.thread_pool"] = config.thread_pool

        cls.config["tools.force_https.on"] = config.force_https

    def register_render_handler(self):
        for handler in render.__all__:
            handler_class = getattr(render, handler)
            cherrypy.tree.mount(handler_class(), handler_class._path,
                                config=Server.static_config)

    def register_rest_view(self):
        for view in rest.__all__:
            view_class = getattr(rest, view)
            cherrypy.tree.mount(view_class(), "/rest/" + view_class._path)

    def start(self):
        ####
        # TODO: subscribe plugin and tool
        ####

        self.register_render_handler()
        self.register_rest_view()

        cherrypy.config.update(Server.config)
        cherrypy.engine.start()
        cherrypy.engine.block()
