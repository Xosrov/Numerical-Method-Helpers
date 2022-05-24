# 2021 Alireza Miryazdi
# Numerical integration using Trapezoidal Rule (with error correction)
import numpy as np

def function(x: float):
    """
        function to integrate
    """
    return np.sin(x)/np.sqrt(1-0.25*np.sin(x)**2)
def dfunction(x:float):
    """
        derivative of function to integrate
        currently MUST be modified manually
        could use other libraries to parametrically derive this also
    """
    return  4*np.cos(x)/((4-np.sin(x)**2)*np.sqrt(1-0.25*np.sin(x)**2))


if __name__ == "__main__":
    x_from = 0
    x_to = np.pi
    numberOfPanes = 4

    h = (x_to - x_from) / (numberOfPanes - 1)
    x = np.linspace(x_from, x_to, numberOfPanes)
    f = function(x)
    f_prime = dfunction(x)

    I_trap = (h/2) * (f[0]+f[-1]+2*sum(f[1:numberOfPanes-1]))
    err_trap = -h**2/12*(f_prime[-1]-f_prime[0])

    print(f"{I_trap=}")
    print(f"{err_trap=}")
    print(f"final sum: {I_trap + err_trap}")
