# TODO Comments

def calculateFibonacci(n):
    fibonnaci = ['1', '1']
    for i in range(2, n):
        fibonnaci.append(str(int(fibonnaci[i - 1]) + int(fibonnaci[i - 2])))

    return ','.join(fibonnaci)


print(calculateFibonacci(50))
