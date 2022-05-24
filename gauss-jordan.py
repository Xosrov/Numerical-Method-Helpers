# 2021 Alireza Miryazdi
# Gauss-Jordan methods for solving a system of equations

import numpy as np
def jordan_gauss_processing(A: np.array, B: np.array):
    """
        array objects for formula in the format Ax = B
        A: multiplier, has to be a square matrix (nxn)
        B: results, has to be single col (nx1)
    """
    matrixLen = len(A)
    # lower triangle zero
    for i in range(matrixLen):  # iterate over rows
        # make diagonal element zero
        initdiag = A[i][i]
        for j in range(i, matrixLen):
            with np.errstate(divide='raise'):
                try:
                    A[i][j] /= initdiag
                except FloatingPointError:
                    print(
                        "Zero encountered in diagonals(multiplier matrix), this isnt supported yet")
                    quit()
        # apply to result
        with np.errstate(divide='raise'):
            try:
                B[i] /= initdiag
            except FloatingPointError:
                print(
                    "Zero encountered in diagonals(answers matrix), this isnt supported yet")
                quit()
        # make element in same column and different rows zero
        for j in range(i+1, matrixLen):
            initdiag2 = A[j][i]
            for k in range(matrixLen):
                A[j][k] -= A[i][k]*initdiag2
            B[j] -= initdiag2 * B[i]

    # upper triangle zero
    for i in reversed(range(matrixLen)):  # reverse iterate over rows
        # make element in same column and different rows zero
        for j in reversed(range(i)):
            initdiag = A[j][i]
            A[j][i] -= initdiag * A[i][i]
            B[j] -= B[i] * initdiag


if __name__ == "__main__":
    print("Solves the value of X in AX=B matrix system")
    print("MAKE SURE YOU MOVE AROUND ELEMENTS TO MAKE MULTIPLIER MATRIX DIAGONALLY DOMINANT")
    multiplier = np.array(
        [
            [3, 1, -1],
            [1, 4, 1],
            [2, 1, 2]
        ], dtype=float)
    results = np.array([
        2,
        12,
        10
    ], dtype=float)
    print(f"A= \n{multiplier}")
    print(f"B= \n{results}")
    jordan_gauss_processing(multiplier, results)
    print("\nAfter processing:")
    print(f"A= \n{multiplier}")
    print(f"B(=X)= \n{results}")
