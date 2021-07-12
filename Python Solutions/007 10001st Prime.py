# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

primes = [2]
currentNumber = 3

while len(primes) < 10001: 
    primeNumber = True

#Only need to test certain numbers, ie the sqrt of current Number

    squaredNumber = math.floor(math.sqrt(currentNumber))

    counter = 0
    while squaredNumber >= primes[counter]:
        counter = counter + 1

    for count in range(counter):
        if currentNumber % primes[count] == 0: 
            primeNumber = False
            break
    if primeNumber == True: 
        primes.append(currentNumber)
    
    currentNumber = currentNumber + 2
print(primes[-1])