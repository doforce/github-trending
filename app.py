from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello github trending!(Preview)'

@app.route('/lang')
async def lang():
   return jsonify({ "path": "lang"})

@app.route('/repo')
async def repo():
   return jsonify({ "path": "repo"})
