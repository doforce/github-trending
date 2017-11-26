# -*- coding:utf-8 -*-
from app import create_app
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app = create_app('default')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
