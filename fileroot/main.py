# import cherrypy
# import sys
# import os
import argparse

from server import Server


COMMAND_DESCRIPTION = """FileRoot

A server for manage file system
-host (String) : Website's IP
-p --port (Int)    : Website's Port
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=COMMAND_DESCRIPTION)
    parser.add_argument("--host", help="IP, default: localhost",
                        default="127.0.0.1")
    parser.add_argument("-p", "--port", help="Port, default: 8080",
                        type=int, default=8080)
    parser.add_argument("--thread-pool", help="Thread pool, how many thread "
                        "will handle clients request", type=int, default=50)
    parser.add_argument("--force-https", help="Redirect http to https, "
                        "default False", action="store_true", default=False)

    args = parser.parse_args()

    Server.parse_config(args)
    server = Server()
    server.start()
