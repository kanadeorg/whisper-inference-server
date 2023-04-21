from flask import Flask, request, jsonify
import os
import base64
import uuid
import whisper

model_path = "./model.pt"

model = whisper.load_model(model_path)

def infer(temp_file):
    result = model.transcribe(os.path.join(temp_file))
    os.remove(temp_file)
    return result["text"]

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    content = request.json
    audio = base64.b64decode(str(content["audio"]))
    id = str(uuid.uuid4())
    temp_file = f"{id}.ogg"
    with open(temp_file, "wb") as b_file:
        b_file.write(audio)
    text = infer(temp_file)
    return jsonify({
        "text": text
    })

app.run(host="0.0.0.0", port=5000)