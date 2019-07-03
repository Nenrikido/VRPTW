"""
    Instances management
"""

import sys
import numpy as np
import generator as gen
from clock import HourClock as Clock


def load(filename: str) -> tuple:
    """
        Loads an instance from a file
        :param filename: File name
        :return: Extracted instance (Size, Vehicles_amount, Matrix, TWs)
    """
    content = open(filename, "r").read()
    lines = content.splitlines()
    meta = lines[0].split()
    size = int(meta[0])
    vehicles_amount = int(meta[1])
    matrix = np.array([[int(j) for j in i.split(',')] for i in lines[1:size + 1]])
    tws = np.array([[Clock(int(j)) for j in i.split(',')] for i in lines[size + 1:]])
    return size, vehicles_amount, matrix, tws


def save(matrix: np.ndarray = None, tws: np.ndarray = None, vehicles_amount: int = None, filename: str = "test.vrp"):
    """
        :param matrix: Matrix
        :param tws: Time windows
        :param vehicles_amount: Amount of vehicles
        :param filename: File Name
    """
    open(filename, "w").write(f"{len(matrix)} {vehicles_amount}\n")
    with open(filename, "a") as f:
        np.savetxt(f, matrix.astype(int), fmt='%i', delimiter=",")
        np.savetxt(f, tws.astype(int), fmt='%i', delimiter=",")
    print("Instance saved")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        size = int(sys.argv[2])
        vehicles_amount = int(sys.argv[3])
        save(gen.generate_matrix(size), gen.generate_time_windows(size), vehicles_amount, sys.argv[1])
    else:
        # save(gen.generate_matrix(), gen.generate_time_windows(), 2)
        print(load("test.vrp"))
