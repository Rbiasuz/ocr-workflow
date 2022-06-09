
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

        img2 = request.files['my_image2']
        img_path2 = "/media/assets/base-images/" + img2.filename
        img2.save(img_path2)

        txt1 = get_text(img_path)
        txt2 = get_text(img_path2)

        l1=[]
        l2=[]

        l1[:0]=txt1
        l2[:0]=txt2

        p = string_distance(l1,l2)

        identifica_img_grupo(img_path)
        identifica_img_grupo(img_path2)

    return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
