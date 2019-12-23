#!/usr/bin/env python3
# STL
import io
import os

# PIP
from flask import Flask, render_template, request, send_file, send_from_directory

# LOCAL
from TextFunctions import check_text, format_text, square_uniform_wrap
from GraphicFunctions import (
    pil_image,
    numpy_array,
    bytesio,
    generate_font_size,
    make_font,
    generate_line_spacing,
    get_text_alignment,
    generate_text_graphic_canvas_size,
    make_canvas,
    draw_text,
    remove_border_from_bicolor_text_graphic,
    generate_border_width,
    add_border,
    add_watermark,
)
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
def index() -> str:
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    quote = request.json.get("quote")
    reduce_punctuation = request.json.get("reduce_punctuation")
    text_passed, warning_msg = check_text(quote, reduce_punctuation)
    return "" if text_passed else warning_msg


@app.route("/generate", methods=["POST"])
def generate():
    def generate_text_graphic(text: str, options: dict) -> io.BytesIO:
        text = format_text(text, options["reduce_punctuation"])
        if options["wrap_text"]:
            text = square_uniform_wrap(text, text.split())
        options.update(color_templates[options["color_template"]])
        font_size = generate_font_size(text)
        font = make_font(font_file, font_size)
        line_spacing = generate_line_spacing(font_size)
        text_alignment = get_text_alignment(text, options["alignment_style"])
        canvas_size = generate_text_graphic_canvas_size(text, font)
        img = make_canvas(canvas_size, options["bg_color"])
        img = draw_text(
            img, text, options["fg_color"], font, line_spacing, text_alignment
        )
        img = remove_border_from_bicolor_text_graphic(
            numpy_array(img), options["bg_color"]
        )
        border_width = generate_border_width(img)
        img = add_border(pil_image(img), border_width, options["bg_color"])
        img = add_watermark(
            img, options["watermark_file"], border_width, options["watermark_position"]
        )
        return bytesio(img)

    quote = request.json.get("quote")
    options = {
        "wrap_text": request.json.get("wrap_text"),
        "reduce_punctuation": request.json.get("reduce_punctuation"),
        "alignment_style": request.json.get("alignment_style"),
        "color_template": request.json.get("color_template"),
        "watermark_position": request.json.get("watermark_position"),
    }
    return send_file(
        generate_text_graphic(quote, options),
        mimetype="image/png",
        attachment_filename="image.png",
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
