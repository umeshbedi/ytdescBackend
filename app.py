from flask import Flask
from transformers import pipeline

app = Flask(__name__)



@app.route("/")
def homepage():
    whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-medium', device=0)
    text = whisper('pandora.mp3')
    return text

if __name__=="__main__":
    app.run(debug=False)