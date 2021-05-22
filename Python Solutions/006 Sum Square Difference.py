# The sum of the squares of the first ten natural numbers is: 385 (1^2 + 2^2......)
# The square of the sum of the first ten natural numbers is (1+2...+10) = 3025
# Difference is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

total = 0
sumOfNumbers = 0

for count in range(1, 101): 
    total = total + count*count
    sumOfNumbers = sumOfNumbers + count

print((sumOfNumbers*sumOfNumbers)-total)
