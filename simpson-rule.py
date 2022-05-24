# 2021 Alireza Miryazdi
# Numerical integration using Simpson's Rule (with error correction)

import numpy as np

def function(x: float):
    """
        function to integrate
    """
    return (1-np.cos(x))/(x**2)
def dfunction(x:float):
    """
        derivative of function to integrate
        currently MUST be modified manually
        could use other libraries to parametrically derive this also
    """
    return (x*np.sin(x)+2*np.cos(x)-2)/(x**3)

if __name__ == "__main__":
    x_from = 1
    x_to = 1000
    numberOfPanes = 5000 # should be an ODD number

    h = (x_to - x_from) / (numberOfPanes - 1)
    x = np.linspace(x_from, x_to, numberOfPanes)
    f = function(x)
    f_prime = dfunction(x)
    I_simp = h/15 * (
        14 * (0.5*(f[0]+f[-1])+sum(f[2:numberOfPanes-2:2])) +
        16 * sum(f[1:numberOfPanes-1:2])
    )
    err_simp = h/15 * h * (f_prime[0] - f_prime[-1])
    print(f"{I_simp=}")
    print(f"{err_simp=}")
    print(f"final sum: {I_simp + err_simp}")
