from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("assets/templates/index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "assets/base-images/" + img.filename
        img.save(img_path)

        p = get_text(img_path)

    return render_template("assets/templates/index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
    app.run(debug = True)