import numpy as np
from scipy.interpolate import interp1d

def complete_curves(path_XYs):
    completed_paths = []
    for path in path_XYs:
        completed_path = []
        for XY in path:
            x = XY[:, 0]
            y = XY[:, 1]
            if len(x) < 2:
                continue
            interp_func_x = interp1d(np.arange(len(x)), x, kind='cubic', fill_value='extrapolate')
            interp_func_y = interp1d(np.arange(len(y)), y, kind='cubic', fill_value='extrapolate')
            x_new = np.linspace(0, len(x) - 1, num=len(x) * 2 - 1)
            y_new = np.linspace(0, len(y) - 1, num=len(y) * 2 - 1)
            x_completed = interp_func_x(x_new)
            y_completed = interp_func_y(y_new)
            completed_path.append(np.column_stack((x_completed, y_completed)))
        completed_paths.append(completed_path)
    return completed_paths
