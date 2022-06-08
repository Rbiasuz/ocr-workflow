
import os
from flask import Flask, render_template, request
from functions import *

app = Flask(__name__,template_folder='templates')

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "/media/assets/base-images/" + img.filename
        img.save(img_path)

        p = get_text(img_path)

    return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
