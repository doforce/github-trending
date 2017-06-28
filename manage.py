from tornado.options import define, options
import tornado.concurrent
from handler import IndexHandler, RepositoryHandler, RepositoryLanguageHandler \
    , DeveloperHandler, DeveloperLanguageHandler

define('port', default=8123, type=int)

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/repo/', RepositoryHandler),
    (r'/repo', RepositoryHandler),
    (r'/repo/(.+)', RepositoryLanguageHandler),
    (r'/developer/', DeveloperHandler),
    (r'/developer', DeveloperHandler),
    (r'/developer/(.+)', DeveloperLanguageHandler),

])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
