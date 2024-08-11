import os
import numpy as np
from google.colab import files
from regularizeCurves import read_csv, smooth_paths, detect_straight_lines, detect_circles, detect_ellipses, detect_rectangles, detect_regular_polygons
from symmetryDetection import detect_symmetry
from curveCompletion import complete_curves
from visualization import plot_shapes
from rasterizeSvg import rasterize_svg

def upload_file():
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename

def process_csv(input_csv, output_dir):
    # Read the CSV file
    path_XYs = read_csv(input_csv)

    # Regularize Curves
    smoothed_paths = smooth_paths(path_XYs, method='spline', s=0.5)
    for i, path in enumerate(smoothed_paths):
        for j, XY in enumerate(path):
            np.savetxt(os.path.join(output_dir, f'regularized_curve_{i}_{j}.csv'), XY, delimiter=',')

    # Detect shapes
    lines = detect_straight_lines(smoothed_paths)
    circles = detect_circles(smoothed_paths)
    ellipses = detect_ellipses(smoothed_paths)
    rectangles = detect_rectangles(smoothed_paths)
    polygons = detect_regular_polygons(smoothed_paths, num_sides=5)  # Example: Detecting pentagons

    # Symmetry Detection
    symmetries = detect_symmetry(smoothed_paths)
    np.savetxt(os.path.join(output_dir, 'symmetry_results.csv'), symmetries, delimiter=',')

    # Curve Completion
    completed_paths = complete_curves(smoothed_paths)
    for i, path in enumerate(completed_paths):
        for j, XY in enumerate(path):
            np.savetxt(os.path.join(output_dir, f'completed_curve_{i}_{j}.csv'), XY, delimiter=',')

    # Visualization
    plot_shapes(smoothed_paths, lines=lines, circles=circles, ellipses=ellipses, rectangles=rectangles, polygons=polygons)

    # Rasterize SVG to PNG
    svg_file = os.path.join(output_dir, 'example.svg')
    png_file = os.path.join(output_dir, 'output.png')
    rasterize_svg(svg_file, png_file)
    print(f'Processed results saved in {output_dir}')

if __name__ == "__main__":
    print("Please upload your input CSV file.")
    input_csv = upload_file()  # Upload file
    output_dir = '/content/output'
    os.makedirs(output_dir, exist_ok=True)
    process_csv(input_csv, output_dir)
