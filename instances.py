"""
    Instances management
"""

import json
import numpy as np
import generator as gen


def load(filename: str) -> np.ndarray:
    """
        Loads an instance from a file
        :param filename: File name
        :return: Extracted instance (2D Matrix)
    """
    return json.open()


def save(matrix: np.ndarray = None, tws: np.ndarray = None, vehicles_amount: int = None, filename: str = "test.json", jsonable: str = None):
    if type(matrix) == np.ndarray:
        matrix = matrix.tolist()
    if type(tws) == np.ndarray:
        tws = tws.tolist()
    if jsonable is None:
        if all(x is not None for x in [matrix, tws, vehicles_amount]):
            jsonable = {
                "matrix": matrix,
                "tws": tws,
                "vehicles_amount": vehicles_amount
            }
        else:
            print("Error, you need to define all the other kwargs except filename if you don't define jsonable", file=__import__("sys").stderr)
            return
        print(jsonable)
    json.dump(open(filename, 'w'), jsonable)


if __name__ == "__main__":
    save(gen.generate_matrix(), gen.generate_time_windows(), 2)
