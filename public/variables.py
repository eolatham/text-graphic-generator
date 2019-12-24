# STL Imports
from os import path
from string import ascii_uppercase

# Program Directories
resource_directory = "resources"

# Resource Files
font_file = path.join(resource_directory, "impact.ttf")
watermark_files = {
    "black": path.join(resource_directory, "watermark_black.png"),
    "white": path.join(resource_directory, "watermark_white.png"),
}

# Text Rules
allowed_letters = ascii_uppercase
allowed_chars = f"""{allowed_letters} \n"!&',-.:;?"""
max_word_count = 60
max_word_len = 30

# Graphic Options
color_templates = {
    "black_on_white": {
        "fg_color": (0, 0, 0),  # rgb black
        "bg_color": (255, 255, 255),  # rgb white
        "watermark_file": watermark_files["black"],
    },
    "white_on_black": {
        "fg_color": (255, 255, 255),  # rgb white
        "bg_color": (0, 0, 0),  # rgb black
        "watermark_file": watermark_files["white"],
    },
    "white_on_red": {
        "fg_color": (255, 255, 255),  # rgb white
        "bg_color": (165, 5, 10),  # rgb red
        "watermark_file": watermark_files["white"],
    },
}
