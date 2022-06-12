import os
from base64 import b64decode
from io import BytesIO

from flask import Flask, jsonify, request
from flask_cors import CORS

from bau.resnet_util import resnet_model, decode_predictions, read_and_prep_images

image_size = 224

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)

fields = ["input_image"]

from bau.util import extract_command_from_request


@app.route("/api/v1/classes", methods=["POST"])
def classify():
    from PIL import Image
    from base64 import encodebytes
    command = extract_command_from_request(request, fields)
    msg = b64decode(command['input_image'])
    buf = BytesIO(msg)
    image = Image.open(buf)
    filename = "sakla.png";
    image.save(filename);
    files = read_and_prep_images(["sakla.png"])
    my_predictions = resnet_model.predict(files)
    labels = decode_predictions(my_predictions, top=1)
    return jsonify({"status": "ok", "class_label": labels[0][0][1], "confidence": str(labels[0][0][2])})


app.run(port=7001)
