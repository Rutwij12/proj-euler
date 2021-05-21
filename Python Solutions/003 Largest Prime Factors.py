#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num = int(600851475143)
primeFactors = []

for count in range(1, num): 
    if num % count == 0:
        num = num / count
        primeFactors.append(count)
    if num == 1: 
        break

print(primeFactors)
