from flask import Flask,jsonify,request

from trending import DEVELOPER, NO_RESULT, REPOSITORY, get_all_language, get_trending

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello github trending!'

@app.route('/lang')
async def lang():
    langs = await get_all_language()
    size = len(langs)
    if size > 0:
        return jsonify({
            'msg': 'suc',
            'count': size,
            'items': langs
        }), 201
    else:
        return jsonify(NO_RESULT), 404

@app.route('/repo')
async def repo():
    return await trending(request.args, REPOSITORY)

@app.route('/developer')
async def developer():
    return await trending(request.args, DEVELOPER)


async def trending(args, start_url: str):
    lang = args.get("lang", None)
    since = args.get("since", None)
    url = start_url
    if lang is not None:
        lang = lang.replace('-shuo', '%23')
        url += lang
    params = None
    if since is not None:
        params = {'since': since}
    result = await get_trending(url=url, params=params)
    if result['count'] > 0:
       return jsonify(result), 201
    else:
        return jsonify(result), 404
    