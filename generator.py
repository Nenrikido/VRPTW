"""
    VRP Input Generator
"""

import numpy as np
import numpy.random as rn
from clock import HourClock as Clock


def generate_matrix(size: int = 10, edges_max_len: int = 6, edges_proba: float = 1.0) -> np.ndarray:
    """
        Generates a matrix of time/distance costs
        :param size: Size of the matrix in height and width (amount of nodes)
        :param edges_max_len: Max length of the generated edges (hours of travel between 2 node)
        :param edges_proba: Proportion of edges (0 being "no edges" and 1 being "maximum edges")
        :return: 2D Matrix
    """

    # Creates an empty 2 dimensional array of width and height `size`
    matrix = np.zeros((size, size), np.int64)

    # Fills the matrix with values taking in account `edges_max_len` and `edges_prop`
    for i in range(1, size):
        for j in range(i):

            # Chooses between if the edge exists or not
            if rn.choice([0, 1], p=[1 - edges_proba, edges_proba]) == 1:
                # Generates a random integer value of maximum `edges_max_len`
                matrix[i, j] = rn.randint(1, edges_max_len)

    # Symmetrizes the matrix
    matrix += matrix.T

    return matrix


def generate_time_windows(pop: int = 10) -> np.ndarray:
    """
        Generates an array of time windows of 6 hours maximum
        :param pop: Population
        :return: Array of time windows
    """

    # Generates starting times (random in [0, 24) hours)
    xs = np.array([Clock(rn.randint(24)) for _ in range(pop)])

    # Generates endings time relative to starting times (delta is random in [6, 12) hours)
    ys = np.array([Clock(x + rn.randint(6, 12)) for x in xs])

    # Merges
    array = np.stack((xs, ys), axis=-1)

    return array


if __name__ == "__main__":
    print(generate_matrix())
    print(generate_time_windows())
