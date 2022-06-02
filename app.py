
import os
from flask import Flask, render_template, request
from functions import *


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']
        p = get_text(img)

    return render_template("index.html", prediction = p)


if __name__ =='__main__':
    port = 5000 #int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
