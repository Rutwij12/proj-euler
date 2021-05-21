# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromeList = []

#For one digit numbers

for x in range(100,1000):
    for y in range(x, 1000):
        possiblePalindrome = str(x*y)

        if possiblePalindrome [::-1] == possiblePalindrome:
             palindromeList.append(int(possiblePalindrome))
             
maxPalindrome = max(palindromeList)
print(maxPalindrome)
