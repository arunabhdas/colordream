def get_palette(filepath):
    with open(filepath) as f:
        palette = f.read().splitlines()

    palette = map(clean, palette)
    return palette

def clean(color):
    color = color.split(",")
    return map(int, color)
