import cairosvg

def svg_to_png(svg_file, png_file):
    cairosvg.svg2png(url=svg_file, write_to=png_file)

def rasterize_svg(svg_path, output_path):
    svg_to_png(svg_path, output_path)
