# Curvetopia
Curvetopia is a project designed to process and analyze curve data using a variety of methods. It provides functionalities for curve regularization, shape detection, symmetry detection, curve completion, and visualization. The project aims to offer a comprehensive toolkit for working with complex curve data and generating insightful visualizations.

# Setup
To set up and run the project, follow these steps:

# Prerequisites
Ensure you have Python 3.10 or higher installed on your system.

# Installation
Clone the Repository

# bash
git clone https://github.com/SivaGuruK/Curvetopia/.git
cd curvetopia
Install Dependencies

# Install the required libraries:
Copy code
pip install -r requirements.txt
Alternatively, you can install dependencies manually:

# bash
pip install numpy scipy matplotlib pandas cairosvg

# Usage
  # Running the Scripts
   Upload Your Input CSV File

  Run the main.py script. It will prompt you to upload your input CSV file.
  !python main.py
  # Processing
  The script will process the CSV file and perform the following tasks:

Regularize curves
Detect shapes (lines, circles, ellipses, rectangles, polygons)
Perform symmetry detection
Complete curves
Visualize the results
Rasterize an SVG file to PNG

# Inputs/Outputs
Input: A CSV file containing curve data.
Output: Several CSV files containing the results of curve regularization, shape detection, and curve completion. An SVG file will be rasterized to PNG.
# Examples
Running the Script
python main.py
Expected Results
After processing, you should see the following:

Regularized curves saved as regularized_curve_i_j.csv
Completed curves saved as completed_curve_i_j.csv
Symmetry results saved as symmetry_results.csv
Visualization displayed using Matplotlib
SVG file saved as output.png
# File Structure
curveCompletion.py: Functions for completing curves.
main.py: Main script that coordinates the processing of curve data.
rasterizeSvg.py: Functions for rasterizing SVG files to PNG.
regularizeCurves.py: Functions for regularizing curves and detecting shapes.
symmetryDetection.py: Functions for detecting symmetry in curves.
visualization.py: Functions for visualizing curves and shapes.
# Dependencies
The project requires the following external libraries:

numpy
scipy
matplotlib
pandas
cairosvg
You can install them using pip or by running the pip install -r requirements.txt command.

