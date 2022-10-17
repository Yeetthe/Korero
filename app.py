from hashlib import new
from pydoc import render_doc
from selectors import EpollSelector
from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect
import sent_analysis

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
            submit_textbox = request.form['content']
            tagged_sentiment = sent_analysis.analysis(submit_textbox)
            return render_template('index.html', submit=submit_textbox, sentiment=tagged_sentiment)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
