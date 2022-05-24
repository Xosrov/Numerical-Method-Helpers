# 2021 Alireza Miryazdi
# Finding polynomial approximation of data using Least Squares method

import numpy as np
import importlib  
foobar = importlib.import_module("gauss-jordan")
# only for polynomial

def getEquationsSetForLeastSquares(polynomialDegree: int, xValues: np.array, yValues: np.array): 
    # get multiplier and results matricies to solve for polynomial
    datalen = len(xValues)
    multipliers = np.array([[0. for _ in range(polynomialDegree)] for _ in range(polynomialDegree)])
    answers = np.array([0. for _ in range(polynomialDegree)])
    for i in range(polynomialDegree):
        for j in range(polynomialDegree):
            if i == j == 0:
                multipliers[i][j] = polynomialDegree
            multipliers[i][j] = sum([xValues[k]**(i+j) for k in range(datalen)])
        answers[i] = sum([yValues[k]*xValues[k]**i for k in range(datalen)])
    return multipliers, answers
if __name__ == "__main__":
    xValues = np.array([
        -1.,
        0.,
        1.,
        2.,
    ], dtype=float)
    yValues = np.array([
        -4.,
        -6.,
        -6.,
        -4.,
    ], dtype=float)
    polynomialDegree = 3
    multipliers, answer = getEquationsSetForLeastSquares(polynomialDegree, xValues, yValues)
    print(multipliers)
    print(answer)
    # solve these equations using other methods
    foobar.jordan_gauss_processing(multipliers, answer)
    print(multipliers)
    print(answer)
    print("therefore, approximation for data is:\n")
    print(' + '.join(f"{answer[i]:.4f}*x^{i}" for i in range(len(answer))))

