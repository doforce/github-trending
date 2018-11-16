from tornado import web, options, ioloop
from handlers import IndexHandler, RepositoryHandler, LanguageHandler, DeveloperHandler

app = web.Application([
    (r'/', IndexHandler),
    (r'/lang', LanguageHandler),
    (r'/repo', RepositoryHandler),
    (r'/developer', DeveloperHandler),
])

if __name__ == '__main__':
    options.parse_command_line()
    app.listen(5000)
    ioloop.IOLoop.current().start()
