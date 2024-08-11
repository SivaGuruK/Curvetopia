import numpy as np

def detect_symmetry(path_XYs):
    def calculate_symmetry(XY):
        center = np.mean(XY, axis=0)
        distances = np.linalg.norm(XY - center, axis=1)
        symmetry_score = np.std(distances)
        return symmetry_score

    symmetries = []
    for path in path_XYs:
        for XY in path:
            symmetry_score = calculate_symmetry(XY)
            symmetries.append(symmetry_score)
    return symmetries
