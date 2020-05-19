#!/usr/bin/env python3
# STL
import io
import os
from typing import List

# PIP
from flask import Flask, render_template, request, send_file, send_from_directory

# LOCAL
import TextFunctions as tf
import GraphicFunctions as gf
from Exceptions import InvalidTextSubmissionException
from variables import font_file, color_templates

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


def generate_text_graphic(text: str, words: List[str], options: dict) -> io.BytesIO:
    text = tf.format_text(text, options["reduce_punctuation"])
    if options["wrap_text"]:
        text = tf.square_uniform_wrap(text, words)
    options.update(color_templates[options["color_template"]])
    font_size = gf.generate_font_size(text)
    font = gf.make_font(font_file, font_size)
    line_spacing = gf.generate_line_spacing(font_size)
    text_alignment = gf.get_text_alignment(text, options["alignment_style"])
    canvas_size = gf.generate_text_graphic_canvas_size(text, font)
    img = gf.make_canvas(canvas_size, options["bg_color"])
    img = gf.draw_text(
        img, text, options["fg_color"], font, line_spacing, text_alignment
    )
    img = gf.remove_border_from_bicolor_text_graphic(
        gf.numpy_array(img), options["bg_color"]
    )
    border_width = gf.generate_border_width(img)
    img = gf.add_border(gf.pil_image(img), border_width, options["bg_color"])
    img = gf.add_watermark(
        img, options["watermark_file"], border_width, options["watermark_position"]
    )
    return gf.bytesio(img)


@app.route("/generate", methods=["POST"])
def generate():
    try:
        text, words = tf.format_text(
            request.json.get("text"), request.json.get("reduce_punctuation")
        )
    except InvalidTextSubmissionException as e:
        return e.message, 400

    options = {
        "wrap_text": request.json.get("text_wrap") == "auto",
        "reduce_punctuation": request.json.get("punctuation_style") == "reduce",
        "alignment_style": request.json.get("alignment_style"),
        "color_template": request.json.get("color_template"),
        "watermark_position": request.json.get("watermark_position"),
    }
    return send_file(
        generate_text_graphic(text, words, options),
        mimetype="image/png",
        attachment_filename="graphic.png",
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
