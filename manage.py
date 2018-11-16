from tornado import web, ioloop
from handlers import IndexHandler, RepositoryHandler, LanguageHandler, DeveloperHandler
from tornado.options import define, options, parse_command_line

define('port', default=5000, help='run on the given port', type=int)
parse_command_line()

app = web.Application([
    (r'/', IndexHandler),
    (r'/lang', LanguageHandler),
    (r'/repo', RepositoryHandler),
    (r'/developer', DeveloperHandler),
])

if __name__ == '__main__':
    app.listen(options.port)
    ioloop.IOLoop.current().start()
