from tornado import web, options, ioloop
from handlers import IndexHandler, RepositoryHandler, LanguageHandler, DeveloperHandler

options.define('port', default=5000, type=int)

app = web.Application([
    (r'/', IndexHandler),
    (r'/lang', LanguageHandler),
    (r'/repo', RepositoryHandler),
    (r'/developer', DeveloperHandler),
])

if __name__ == '__main__':
    options.parse_command_line()
    app.listen(options.port)
    ioloop.IOLoop.current().start()
