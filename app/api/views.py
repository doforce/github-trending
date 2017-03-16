from . import api
from flask import jsonify, request
from ..scrapy import get_trending, TRENDING, DEVELOPERS


@api.route('/')
def index():
    return 'ok'


@api.route('/trending/<language>')
def trending_lang(language):
    since = request.args.get('since', None)
    result = get_trending(url=TRENDING + language, params={'since': since})
    return jsonify(result)


@api.route('/trending/')
def trending():
    since = request.args.get('since', None)
    result = get_trending(url=TRENDING, params={'since': since})
    return jsonify(result)


@api.route('/test')
def test():
    # result = get_trending(url='https://github.com/trending/nl?since=monthly')
    # return jsonify(result)
    return 'ok'
