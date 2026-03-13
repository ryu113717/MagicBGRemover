from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        file = request.files["image"]

        img = Image.open(file)

        output = remove(img)

        img_io = io.BytesIO()
        output.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png")

    return render_template("index.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
