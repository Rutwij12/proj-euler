# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

num = int(1000)
total = 0

#For Loop iterates starting from 0 to 1000 with step 3
#Each time it iterates the value of total increases by 3 (sum of all multiples of 3)
for count in range(0,num,3):
    total = total+count

#For Loop iterates starting from 0 to 1000 with step 5
#Each time it iterates the value of total increases by 5 (sum of all multiples of 5)
#To prevent double values the if statement ensures the number being added is not a multiple of 3 
for count in range(0,num,5):
    if (count % 3 == 0):
        total = total
    else:
        total = total+count    

print(total)