from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


lang = [
  { 
    'id':1,
    'emoji':'😀',
    'name':'Grinning'
  },
  {
    'id':2,
    'emoji':'😃',
    'name':'Grinning2'
  },
  {
    'id':3,
    'emoji':'😄',
    'name':'Grinning_with_smile'
  },
  {
    'id':4,
    'emoji':'😁',
    'name':'Beaming_with_smile'
  }, 
  {
  	'id':5,
  	'emoji':'😆',
  	'name':'Grinning_and_squinting_face'
  }

]

@app.route('/api', methods=['GET'])
def api_all():
    return jsonify(lang)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)