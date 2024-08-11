import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline

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

def smooth_paths(path_XYs, method='spline', s=0.5):
    smoothed_paths = []
    for path in path_XYs:
        smoothed_path = []
        for XY in path:
            x = XY[:, 0]
            y = XY[:, 1]
            if len(x) < 5:
                continue
            if method == 'spline':
                t = np.arange(len(x))
                spline_x = UnivariateSpline(t, x, s=s)
                spline_y = UnivariateSpline(t, y, s=s)
                x_smooth = spline_x(t)
                y_smooth = spline_y(t)
                smoothed_path.append(np.column_stack((x_smooth, y_smooth)))
        smoothed_paths.append(smoothed_path)
    return smoothed_paths

def detect_straight_lines(path_XYs):
    lines = []
    for path in path_XYs:
        for XY in path:
            if len(XY) < 2:
                continue
            x = XY[:, 0]
            y = XY[:, 1]
            A = np.vstack([x, np.ones(len(x))]).T
            m, c = np.linalg.lstsq(A, y, rcond=None)[0]
            lines.append((m, c))
    return lines

def fit_circle(x, y):
    def residuals(*args):
        x, y, params = args
        xc, yc, R = params
        return np.sqrt((x - xc)**2 + (y - yc)**2) - R

    x_m = np.mean(x)
    y_m = np.mean(y)
    R = np.mean(np.sqrt((x - x_m)**2 + (y - y_m)**2))
    initial_guess = [x_m, y_m, R]
    params, _ = curve_fit(residuals, x, y, np.zeros_like(x), p0=initial_guess)
    return params

def detect_circles(path_XYs):
    circles = []
    for path in path_XYs:
        for XY in path:
            x = XY[:, 0]
            y = XY[:, 1]
            if len(x) < 3:
                continue
            params = fit_circle(x, y)
            circles.append(params)
    return circles

def fit_ellipse(x, y):
    def residuals(*args):
        x, y, params = args
        a, b, x0, y0, theta = params
        x_rot = (x - x0) * np.cos(theta) + (y - y0) * np.sin(theta)
        y_rot = -(x - x0) * np.sin(theta) + (y - y0) * np.cos(theta)
        return ((x_rot / a)**2 + (y_rot / b)**2 - 1)

    initial_guess = [1, 1, np.mean(x), np.mean(y), 0]
    params, _ = curve_fit(residuals, x, y, np.zeros_like(x), p0=initial_guess)
    return params
def detect_ellipses(path_XYs):
    ellipses = []
    for path in path_XYs:
        for XY in path:
            x = XY[:, 0]
            y = XY[:, 1]
            if len(x) < 5:
                continue
            params = fit_ellipse(x, y)
            ellipses.append(params)
    return ellipses

def detect_rectangles(path_XYs):
    import cv2

    rectangles = []
    for path in path_XYs:
        for XY in path:
            XY = np.array(XY, dtype=np.float32)
            if len(XY) < 4:
                continue
            xy = np.column_stack((XY[:, 0], XY[:, 1]))
            hull = cv2.convexHull(xy, returnPoints=True)
            if len(hull) < 4:
                continue
            rect = cv2.minAreaRect(hull)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            rectangles.append(box)
    return rectangles

def detect_regular_polygons(path_XYs, num_sides=3):
    polygons = []
    for path in path_XYs:
        for XY in path:
            XY = np.array(XY)
            if len(XY) < num_sides:
                continue
            x = XY[:, 0]
            y = XY[:, 1]
            distances = np.sqrt(np.diff(x, append=x[0])**2 + np.diff(y, append=y[0])**2)
            if np.allclose(distances, distances[0], rtol=0.1):
                polygons.append(XY)
    return polygons
