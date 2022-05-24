# 2021 Alireza Miryazdi
# Inverse Interpolation to find value of function at arbitrary position

import numpy as np
def interpolate(functionValues: np.array, inputValues: np.array, targetValue):
    datalen = len(inputValues)
    print("x({}) = {} WHERE:".format(
        targetValue,
        ' + '.join(
            [f"{inputValues[i]}P_{i}({targetValue})" for i in range(datalen)])
    ))
    Pn = np.array([0. for _ in range(datalen)])
    for i in range(datalen):
        surat = 1
        makhraj = 1
        for j in range(datalen):
            if i == j: 
                continue
            surat *= targetValue-functionValues[j]
            makhraj *= functionValues[i]-functionValues[j]
        Pn[i] = surat/makhraj
        print(f"P_{i}({targetValue}) = {Pn[i]}")
    answer = sum([inputValues[i]*Pn[i] for i in range(datalen)])
    print(f"interpolation x value where f(x) = {targetValue} is {answer:.5f}")

if __name__ == "__main__":
    functionValues = np.array([ # f(x)
        -0.35668,
        -0.23524,
        -0.06550,
        0.17215
        ], dtype=float)
    inputValues = np.array([  # (x)
        1.05,
        1.10,
        1.15,
        1.20
    ], dtype=float)
    targetValue = 0 # find where f(x) = targetValue
    interpolate(functionValues, inputValues, targetValue)

