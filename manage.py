from tornado.options import define, options
import tornado.httpserver
import tornado.httpclient
import tornado.web
import tornado.options
import tornado.ioloop
import tornado.gen
from scrapy import get_trending, get_developers, TRENDING
import tornado.concurrent
import json

define('port', default=8123, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write('Hello world!')


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        response = yield tornado.gen.Task(self.get_result, self.get_since())
        self.write(json.dumps(response, indent=2))
        self.finish('Ok')

    def get_since(self):
        return self.get_argument('since', None)

    @tornado.gen.coroutine
    def get_result(self, params):
        pass


class TrendingHandler(BaseHandler):
    @tornado.gen.coroutine
    def get_result(self, params):
        return get_trending(params=params)


class TrendingLanguageHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, lang):
        response = yield tornado.gen.Task(self.get_result_language, self.get_since(), lang)
        self.write(json.dumps(response, indent=2))
        self.finish('Ok')

    @tornado.gen.coroutine
    def get_result_language(self, params, lang):
        return get_trending(url=TRENDING + lang, params=params)


class DeveloperHandler(BaseHandler):
    @tornado.gen.coroutine
    def get_result(self, params):
        return get_developers(params=params)


app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/trending/', TrendingHandler),
    (r'/trending', TrendingHandler),
    (r'/trending/(.+)', TrendingLanguageHandler),
    (r'/developer/', DeveloperHandler),
    (r'/developer', DeveloperHandler),
])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
