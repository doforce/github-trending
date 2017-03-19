from tornado.options import define, options
import tornado.concurrent
from handler import IndexHandler, RepositoryHandler, RepositoryLanguageHandler \
    , DeveloperHandler, DeveloperLanguageHandler, TestHandler

define('port', default=8123, type=int)

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/api/repo/', RepositoryHandler),
    (r'/api/repo', RepositoryHandler),
    (r'/api/repo/(.+)', RepositoryLanguageHandler),
    (r'/api/dev/', DeveloperHandler),
    (r'/api/dev', DeveloperHandler),
    (r'/api/dev/(.+)', DeveloperLanguageHandler),
    (r'/api/test', TestHandler),
])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
