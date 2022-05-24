# 2021 Alireza Miryazdi
# Gauss-Seidel method for solving system of equations with initial guesses

import numpy as np


def iteration(multiplier: np.array, results: np.array, initialGuesses: np.array) -> None:
    for i in range(len(initialGuesses)):
        temp = results[i]/multiplier[i][i]
        for j in range(len(multiplier[i])):
            if j == i:
                continue
            temp -= multiplier[i][j]/multiplier[i][i]*initialGuesses[j]
        initialGuesses[i] = temp
def solve(iterations: int, multiplier: np.array, results: np.array, initialGuesses: np.array, t0=1) -> None:
    print(f"For iteration {t0}:")
    oldGuesses = np.copy(initialGuesses)
    iteration(multiplier, results, initialGuesses)
    print(f"\t{initialGuesses}")
    for i in range(len(initialGuesses)):
        relativeConvergence = abs((initialGuesses[i]-oldGuesses[i])/initialGuesses[i])
        print(f"\tfor x({i+1}) convergence is: {relativeConvergence:e}")
    if t0 == iterations:
        return
    solve(iterations, multiplier, results, initialGuesses, t0+1)
if __name__ == "__main__":
    print("MAKE SURE YOU MOVE AROUND ELEMENTS TO MAKE MATRIX DIAGONALLY DOMINANT")
    multiplier = np.array(
        [
            [4., 2., 6.],
            [2., 6., 8.,],
            [6., 8., 18.,]
        ], dtype=float)
    results = np.array([
        -20.,
        -10.,
        -26.
    ], dtype=float)
    initialGuesses = np.array([
        -2.,
        -2.,
        1.
    ], dtype=float)
    solve(20, multiplier, results, initialGuesses)
