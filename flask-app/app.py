# app.py
from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

major = [
    {
        "id":1,
        "name": "Information Technology",
        "shortname":"IT"
    },
    {
        "id":2,
        "name": "Computer Network Technology",
        "shortname":"CNT"
    },
]

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/major')
def major_api():
    return jsonify(major)

if __name__=="__main__":
    app.run(debug=False)


