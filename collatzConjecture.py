# collatzConjecture.py uses the Collatz Conjecture algorithm to find the
# number of steps it takes to get to 1 from a number following these rules:
# Start with a number n > 1. Find the number of steps it takes to reach one
# using the following process: If n is even, divide it by 2. If n is odd,
# multiply it by 3 and add 1

# divides by 2 if current n is an even number
def currentEven(n):
    return n / 2

# multiplies by 3 and adds 1 of current n is uneven
def currentUneven(n):
    return n * 3 + 1

# calls the calculating functions and counts number of steps
def collatz(n):
    number_of_steps = 0
    while n > 1:
        if n % 2 == 0:
            n = currentEven(n)
        else:
            n = currentUneven(n)
        number_of_steps += 1
    return number_of_steps