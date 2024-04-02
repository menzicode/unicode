from fontTools.ttLib import TTFont
import os
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE = 175

def get_codepoints(font_path):
    """
    Finds Unicode codepoints supported by a font file 
    and returns them as a set to avoid duplication
    """
    font = TTFont(font_path)
    codepoints = []

    for table in font['cmap'].tables:
        if table.isUnicode():
            codepoints.extend(table.cmap.keys())

    return sorted(set(codepoints))

def draw_codepoint(codepoint, font_object, font_name):
    """
    Creates image of codepoint in a given 
    font and saves it to relevant directory
    """
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

    filename = f'{directory}/{font_name}.png'

    image.save(filename)

def enumerate_files(directory):
    file_paths = []  # List to store file paths
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)  
            file_paths.append(file_path)
    return file_paths

if __name__ == '__main__':

    fontdir = 'Ubuntu/'
    
    print(f'Font name: {fontdir.split("/")[0]}')

    paths = enumerate_files(fontdir)

    print(f'Found {paths} fonts')
    
    for path in enumerate_files(fontdir):
        fname = path.split('/')[-1]

        try:
            font = ImageFont.truetype(
                        font=path,
                        size=FONT_SIZE,
                        index=0,
                        encoding='unic'
                    )
        except:
            print(f'Error parsing {fname}')
            continue

        print(f'Font: {fname}')

        try:
            codepoints = get_codepoints(path)
        except:
            print(f'Error parsing {fname}')
            continue

        print(f'Found {len(codepoints)} codepoints for font {fname}')
        
        print("Saving images to directory ~/image_data/")

        ctr = 0
        for codepoint in codepoints:
            unicp = format(codepoint, "04x")
            draw_codepoint(codepoint, font, fname.split('.')[0])
            ctr += 1
        print(f'Finished saving {ctr} images\n')
