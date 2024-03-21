from flask import Flask, request, jsonify
import util
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/classify_image', methods=['GET','POST'])
def classify_image():
    image_datas = request.form['image_data']
    print(image_datas)
    response = jsonify(util.classify_image(image_datas))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True,port=5000)