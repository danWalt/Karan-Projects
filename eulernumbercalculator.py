# This code calculates euler number ("e") up to the prec number minus one
# given after the decimal point. The higher the given "n" is, the more
# accurate the calculation is. The higher "prec" is, the more digits
# after the decimal point are shown

from decimal import Decimal as Dec, getcontext as gc
from math import factorial


def eulerNumber(n=100, prec=100):
    gc().prec = prec
    e = 0
    for i in range(n):
        e += Dec(1 / factorial(i))
    return Dec(e)


print(eulerNumber())
