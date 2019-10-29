from flask import Flask, render_template
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',moji = "日常")

@app.route('/<moji>')
def withmoji(moji):
    return render_template('index.html',moji = urllib.parse.unquote(moji))

if __name__ == "__main__":
    app.run(threaded=True)