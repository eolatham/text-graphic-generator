#!/usr/bin/env python3
# STL
import os

# PIP
from flask import Flask, render_template, request, send_file, send_from_directory

# LOCAL
from worker import worker

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
def index() -> str:
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    result = worker(request.json.get("quote"))
    if isinstance(result, str):
        return (result, 204)
    else:
        return send_file(
            result,
            mimetype="image/png",
            attachment_filename="image.png",
            as_attachment=True,
        )
