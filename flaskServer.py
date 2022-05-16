from flask import Flask, request
import json
import base64
from Machine_Learning import predict
from pathlib import Path
import os

app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello():
    return 'i am python server'

@app.route('/image',methods=['POST'])
def creat_image():
    encoded_string = json.loads(request.data)
    encoded_string = encoded_string["Base64_image"]
    imgdata = base64.b64decode(encoded_string)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    path = Path(filename)
    str = predict(path)
    os.remove(path)
    return str

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/get_txt', methods=['GET'])
def process_txt():
    data = json.loads(request.data)
    print (data)
    return data

if __name__ == "__main__":
    app.run()