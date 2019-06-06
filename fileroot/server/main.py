import os
import cherrypy

from .render import IndexHandler


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

    def start(self):
        ####
        # TODO: subscribe plugin and tool
        ####

        cherrypy.tree.mount(IndexHandler(), IndexHandler._path,
                            config=Server.static_config)

        cherrypy.config.update(Server.config)
        cherrypy.engine.start()
        cherrypy.engine.block()
