#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num = 600851475143
primeFactors = [1]

for count in range(2, num - 1): 
    if num % count == 0:

            temp = True

            while temp == True: 
                primeFactors.append(count)
                for i in range(1, len(primeFactors) - 2):

                    if count % primeFactors[i] != 0:
                        temp = True
                    else:
                        temp = False
                        try: 
                            primeFactors.remove(count)
                        except: 
                            print("Already been removed")
                        
               
                temp = False
        
print(primeFactors)
        
    
 