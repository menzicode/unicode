from fontTools.ttLib import TTFont
import os
from PIL import Image, ImageDraw, ImageFont

FONT_NAME = 'OpenSans-Regular'
FONT_SIZE = 175

def get_codepoints(font_path):
    font = TTFont(font_path)
    codepoints = []

    for table in font['cmap'].tables:
        if table.isUnicode():
            codepoints.extend(table.cmap.keys())

    return sorted(set(codepoints))

font = ImageFont.truetype(
            font='open_sans/static/OpenSans-Regular.ttf',
            size=FONT_SIZE,
            index=0,
            encoding='unic'
        )

codepoints = get_codepoints('open_sans/static/OpenSans-Regular.ttf')

def draw_codepoint(codepoint, font_object):
    image = Image.new('RGB', (256, 256), 'white')
    draw = ImageDraw.Draw(image)

    character = chr(codepoint)
    left, _top, right, _bottom = draw.textbbox(
                (0,0),
                character,
                font_object,
                font_size=FONT_SIZE
            )

    text_x = (256 - (right - left)) / 2

    draw.text((text_x, 0), character, fill='black', font=font)

    directory = f'image_data/{format(codepoint, "04x")}'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f'{directory}/{FONT_NAME}.png'

    image.save(filename)

for codepoint in codepoints:
    unicp = format(codepoint, "04x")
    draw_codepoint(codepoint, font)
