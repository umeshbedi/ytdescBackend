from flask import Flask
from transformers import pipeline
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium')
    filename = "pandora.mp3"
    appRoot = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(appRoot, 'static', filename)
    text = whisper(filePath)
    return text

if __name__=="__main__":
    app.run(debug=True)