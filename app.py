from flask import Flask
from transformers import pipeline

app = Flask(__name__)

whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium', device=0)

@app.route("/")
def homepage():
    text = whisper('pandora.mp3')
    return text

if __name__=="__main__":
    app.run(debug=False)