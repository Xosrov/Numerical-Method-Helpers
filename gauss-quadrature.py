# 2021 Alireza Miryazdi
# Gauss-Quadrature method for numerial integration

import numpy as np

def function(x: float):
    """
        function to integrate
    """
    return x * np.log(np.sin(x))

if __name__ == "__main__":
    polynomial_sample_degree = 24 # the more this is the more precise the answer
    # x range of integral
    x_from = 0
    x_to = 1
    weightsAndZeros = np.polynomial.legendre.leggauss(polynomial_sample_degree)
    zeros = weightsAndZeros[0]
    weights = weightsAndZeros[1]
    print("zeta: \n\t{}\nw: \n\t{}".format(
        '\n\t'.join([str(i) for i in zeros]),
        '\n\t'.join([str(i) for i in weights])
    ))
    x_k = (x_to+x_from)/2 + (x_to-x_from)/2*zeros
    print("x values are:\n\t{}".format(
        '\n\t'.join([str(i) for i in x_k])
    ))

    f = function(x_k)

    print("f(x) values are:\n\t{}".format(
        '\n\t'.join([str(i) for i in f])
    ))

    I_gq = (x_to-x_from)/2 * sum(weights*f)
    print("Final value of I_bar is: {}".format(str(I_gq)))