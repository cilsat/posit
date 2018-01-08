#!/usr/bin/env python

import api
import sys
import json
import tornado.ioloop
from tornado_json.routes import get_routes
from tornado_json.application import Application


def main():
    routes = get_routes(api)
    print("Routes\n======\n\n" + json.dumps(
        [(url, repr(rh)) for url, rh in routes])
    )
    app = Application(routes=routes, settings={}, generate_docs=True)
    app.listen(6060)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
