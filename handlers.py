from abc import ABC

from tornado.web import RequestHandler

from tornado_cors import CorsMixin

from trending import get_trending, NO_RESULT, REPOSITORY, DEVELOPER, get_all_language


class IndexHandler(CorsMixin, RequestHandler, ABC):
    CORS_ORIGIN = '*'

    def get(self):
        self.finish('Hello github trending!')


class LanguageHandler(CorsMixin, RequestHandler, ABC):
    CORS_ORIGIN = '*'

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    async def get(self, *args, **kwargs):
        langs = await get_all_language()
        size = len(langs)
        if size > 0:
            self.set_status(201)
            self.finish({
                'msg': 'suc',
                'count': size,
                'items': langs
            })
        else:
            self.set_status(404)
            self.finish(NO_RESULT)


class RepositoryHandler(CorsMixin, RequestHandler, ABC):
    CORS_ORIGIN = '*'

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    async def get(self, *args, **kwargs):
        await trending(self, REPOSITORY)


class DeveloperHandler(CorsMixin, RequestHandler, ABC):
    CORS_ORIGIN = '*'

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    async def get(self, *args, **kwargs):
        await trending(self, DEVELOPER)


async def trending(req: RequestHandler, start_url: str):
    lang = req.get_argument("lang", None)
    since = req.get_argument("since", None)
    url = start_url
    if lang is not None:
        lang = lang.replace('-shuo', '%23')
        url += lang
    params = None
    if since is not None:
        params = {'since': since}
    result = await get_trending(url=url, params=params)
    if result['count'] > 0:
        req.set_status(201)
    else:
        req.set_status(404)
    req.finish(result)
