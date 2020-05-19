#!/usr/bin/env python3
# STL
import os

# PIP
from flask import Flask, render_template, request, send_file, send_from_directory

# LOCAL
from TextFunctions import format_text
from GraphicFunctions import generate_text_graphic
from Exceptions import InvalidTextSubmissionException

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="images/vnd.microsoft.icon",
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        text, words = format_text(
            request.json.pop("text"),
            request.json.pop("reduce_punctuation"),
            request.json.pop("wrap_text"),
        )
        return send_file(
            generate_text_graphic(text, words, **request.json),
            mimetype="image/png",
            attachment_filename="graphic.png",
            as_attachment=True,
        )
    except InvalidTextSubmissionException as e:
        return e.message, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
