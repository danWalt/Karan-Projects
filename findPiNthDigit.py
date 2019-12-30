# This code calculates Pi and shows it up to the prec digit

from decimal import Decimal as Dec, getcontext as gc


def pi(n, prec=100):
    L, X, M, K, S, C = 13591409, 1, 1, 6, 13591409, 426880 * Dec(10005).sqrt()
    gc().prec = prec
    for i in range(1, n + 1):
        M = (K ** 3 - 16 * K) * M // (i + 1) ** 3
        L += 545140134
        X *= (-262537412640768000)
        S += Dec(M * L) / X
        K += 12
    pi = Dec(C / S)
    return pi