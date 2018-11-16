from flask import jsonify, request

from . import main
from trending import get_trending, REPOSITORY, DEVELOPER, get_all_language


@main.route('/')
def index():
    return 'Hello GitHub Trending!'


@main.route('/repo', methods=['GET'])
def repo():
    return trending(REPOSITORY)


@main.route('/developer', methods=['GET'])
def developer():
    return trending(DEVELOPER)


def trending(start_url):
    lang = request.args.get('lang')
    since = request.args.get('since')
    url = start_url
    if lang is not None:
        lang = lang.replace('-shuo', '%23')
        url += lang
    params = None
    if since is not None:
        params = {'since': since}
    result = get_trending(url=url, params=params)
    if result['count'] > 0:
        return jsonify(result), 201
    else:
        return jsonify(result), 404


@main.route('/lang', methods=['GET'])
def languages():
    langs = get_all_language()
    size = len(langs)
    if size > 0:
        return jsonify({
            'msg': 'suc',
            'count': size,
            'items': langs
        }), 201
    else:
        return jsonify({
            'msg': 'Unavialiable.',
            'count': 0,
            'items': []
        }), 404
