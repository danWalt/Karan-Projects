# This code calculates the prime factors of a given n entered by the user


print('Pick a number you want to see the prime factorization of:')
n = int(input())
listofprimes = []
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        listofprimes.append(int(i))
        n //= i
if n > 1:
    listofprimes.append(int(n))
print(listofprimes)
