#!/usr/bin/env python3
# STL Imports
import io
from random import choice
from logging import getLogger

# Local Imports
from LoggingFunctions import init_logger
from TextFunctions import format_text, check_text, square_uniform_wrap
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
from variables import (
    font_files,
    reduce_punctuation,
    text_alignment_style,
    watermark_position,
    graphic_templates,
)

LOG = getLogger(__name__)


def gather_text_graphic_info(text: str) -> dict:
    info = dict()
    info["text"] = text
    info["font_file"] = choice(font_files)
    info["alignment_style"] = text_alignment_style
    info["watermark_position"] = watermark_position
    info.update(choice(graphic_templates))
    return info


def generate_text_graphic(info: dict) -> io.BytesIO:
    font_size = generate_font_size(info["text"])
    font = make_font(info["font_file"], font_size)
    line_spacing = generate_line_spacing(font_size)
    text_alignment = get_text_alignment(info["text"], info["alignment_style"])
    canvas_size = generate_text_graphic_canvas_size(info["text"], font)
    img = make_canvas(canvas_size, info["bg_color"])
    img = draw_text(
        img, info["text"], info["fg_color"], font, line_spacing, text_alignment
    )
    img = remove_border_from_bicolor_text_graphic(numpy_array(img), info["bg_color"])
    border_width = generate_border_width(img)
    img = add_border(pil_image(img), border_width, info["bg_color"])
    img = add_watermark(
        img, info["watermark_file"], border_width, info["watermark_position"]
    )
    return bytesio(img)


def worker(quote: str) -> io.BytesIO or str:
    init_logger()
    text, words = format_text(quote, reduce_punctuation)
    text_passed, warning_msg = check_text(text, words)
    if text_passed:
        wrapped_text = square_uniform_wrap(text, words)
        info = gather_text_graphic_info(wrapped_text)
        img = generate_text_graphic(info)
        return img
    else:
        LOG.warning(warning_msg)
        return warning_msg
