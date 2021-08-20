from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


lang = [
  { 
    'id':0,
    'emoji':'😀',
    'name':''
  },
  {
    'id':1,
    'emoji':'😀',
    'name':''
  }
]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(lang)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)