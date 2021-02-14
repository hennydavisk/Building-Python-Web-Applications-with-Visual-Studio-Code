from flask import Flask, render_template
from textblob import TextBlob
app = Flask(__name__)


@app.route('/<message>')
def index(message):
    sentiment = "Positive"
    if(TextBlob(message).sentiment.polarity < 0.0):
      sentiment = "Negative"
    return app.make_response(sentiment)

