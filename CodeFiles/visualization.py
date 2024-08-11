import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from google.colab import files

def upload_csv():
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename

def read_csv(csv_path):
    np_path_XYs = np.genfromtxt(csv_path, delimiter=',')
    path_XYs = []
    for i in np.unique(np_path_XYs[:, 0]):
        npXYs = np_path_XYs[np_path_XYs[:, 0] == i][:, 1:]
        XYs = []
        for j in np.unique(npXYs[:, 0]):
            XY = npXYs[npXYs[:, 0] == j][:, 1:]
            XYs.append(XY)
        path_XYs.append(XYs)
    return path_XYs

def plot_shapes(path_XYs, lines=[], circles=[], ellipses=[], rectangles=[], polygons=[]):
    fig, ax = plt.subplots(tight_layout=True, figsize=(10, 10))
    for i, path in enumerate(path_XYs):
        for XY in path:
            ax.plot(XY[:, 0], XY[:, 1], c='black', linewidth=2)
    for line in lines:
        m, c = line
        x_vals = np.linspace(-10, 10, 100)
        y_vals = m * x_vals + c
        ax.plot(x_vals, y_vals, c='red', linestyle='--')
    for circle in circles:
        xc, yc, R = circle
        circle_plot = plt.Circle((xc, yc), R, color='green', fill=False)
        ax.add_artist(circle_plot)
    for ellipse in ellipses:
        a, b, x0, y0, theta = ellipse
        ellipse_plot = plt.Ellipse((x0, y0), 2*a, 2*b, angle=np.degrees(theta), color='blue', fill=False)
        ax.add_artist(ellipse_plot)
    for rect in rectangles:
        rect_plot = plt.Polygon(rect, closed=True, fill=None, edgecolor='purple')
        ax.add_patch(rect_plot)
    for polygon in polygons:
        poly_plot = plt.Polygon(polygon, closed=True, fill=None, edgecolor='orange')
        ax.add_patch(poly_plot)
    ax.set_aspect('equal')
    plt.title('Detected Shapes')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
