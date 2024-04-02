from fontTools.ttLib import TTFont

def get_codepoints(font_path):
    font = TTFont(font_path)
    codepoints = []

    for table in font['cmap'].tables:
        if table.isUnicode():
            codepoints.extend(table.cmap.keys())

    return sorted(set(codepoints))
