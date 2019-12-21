# STL Imports
import io
from typing import Tuple
from random import choice

# PIP Imports
from PIL import Image, ImageFont, ImageDraw, ImageOps
from numpy import array, argwhere


def pil_image(img: array) -> Image.Image:
    return Image.fromarray(img)


def numpy_array(img: Image.Image) -> array:
    return array(img)


def bytesio(img: Image.Image) -> io.BytesIO:
    img_bytesio = io.BytesIO()
    img.save(img_bytesio, "PNG", quality=100)
    img_bytesio.seek(0)
    return img_bytesio


def generate_font_size(text: str) -> int:
    return int(-0.3 * len(text) + 400)


def make_font(file: str, size: int) -> ImageFont:
    return ImageFont.truetype(file, size)


def generate_line_spacing(font_size: int) -> int:
    return font_size // 12


def get_text_alignment(text: str, style: str) -> str:
    assert style in ["smart", "random", "left", "right", "center"]

    if style == "smart":
        if len(text.split("\n")) in range(5):
            return "center"
        elif "..." in text:
            return "left"
        else:
            return choice(["left", "right"])
    elif style == "random":
        return choice(["left", "right", "center"])
    else:
        return style


def generate_text_graphic_canvas_size(text: str, font: ImageFont) -> Tuple[int, int]:
    lines = text.split("\n")
    num_lines = len(lines)
    longest_line = max(lines, key=len)
    text_size = font.getsize(longest_line)
    return int(2 * text_size[0]), int(1.5 * text_size[1] * num_lines)


def make_canvas(size: Tuple[int, int], color: Tuple[int, int, int]) -> Image.Image:
    return Image.new("RGB", size, color)


def draw_text(
    img: Image.Image,
    text: str,
    color: Tuple[int, int, int],
    font: ImageFont,
    spacing: int,
    alignment: str,
) -> Image.Image:
    draw = ImageDraw.Draw(img)
    draw.multiline_text((0, 0), text, color, font, None, spacing, alignment)
    return img


def remove_border_from_bicolor_text_graphic(
    img: array, border_color: Tuple[int, int, int]
) -> array:
    mask = img != border_color
    coords = argwhere(mask)
    a, b = coords.min(axis=0)[:2]
    c, d = coords.max(axis=0)[:2]
    a, b, c, d = a + 1, b + 1, c + 1, d + 1
    return img[a:c:, b:d:]


def generate_border_width(img: array) -> int:
    size = img.shape[:2]
    return min(size) // 8


def add_border(
    img: Image.Image, width: int, color: Tuple[int, int, int]
) -> Image.Image:
    return ImageOps.expand(img, width, color)


def add_watermark(
    img: Image.Image, file: str, width: int, position: str
) -> Image.Image:
    assert position in [
        "none",
        "top_left",
        "top_right",
        "bottom_left",
        "bottom_right",
        "all",
    ]

    if position == "none":
        return img

    watermark = Image.open(file).resize((width, width), resample=Image.LANCZOS)
    positions = {
        "top_left": (0, 0),
        "top_right": (img.size[0] - width, 0),
        "bottom_left": (0, img.size[1] - width),
        "bottom_right": (img.size[0] - width, img.size[1] - width),
    }
    if position == "all":
        for p in positions.values():
            img.paste(watermark, p, watermark)
    else:
        img.paste(watermark, positions[position], watermark)
    return img
