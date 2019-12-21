# STL Imports
from os import path
from string import ascii_uppercase


# Program Directories
resource_directory = "resources"  # it's best not to change this

# Resource Files
font_files = [  # add your own — a font in this list will be chosen randomly for each graphic
    path.join(resource_directory, "impact.ttf")
]
watermark_files = {  # add your own — these files should be integrated within the graphic_templates variable below
    "black": path.join(resource_directory, "watermark_black.png"),
    "white": path.join(resource_directory, "watermark_white.png"),
}

# Text Rules
reduce_punctuation = (  # True or False — True will strip some punctuation from the beginning and end of each text
    True
)
allowed_letters = ascii_uppercase
allowed_chars = f"""{allowed_letters} "!&',-.:;?"""
max_word_count = 60
max_word_len = 30

# Graphic Options
text_alignment_style = "smart"  # smart, random, left, right, or center
watermark_position = (  # none, top_left, top_right, bottom_left, bottom_right, or all
    "all"
)
graphic_templates = [
    {
        "bg_color": (255, 255, 255),  # rgb white
        "fg_color": (0, 0, 0),  # rgb black
        "watermark_file": watermark_files["black"],  # looks good on light bg_color
    },
    {
        "bg_color": (0, 0, 0),  # rgb black
        "fg_color": (255, 255, 255),  # rgb white
        "watermark_file": watermark_files["white"],  # looks good on dark bg_color
    },
    {
        "bg_color": (165, 5, 10),  # rgb red
        "fg_color": (255, 255, 255),  # rgb white
        "watermark_file": watermark_files["white"],  # looks good on dark bg_color
    },
]
