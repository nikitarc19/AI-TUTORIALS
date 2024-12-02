# Number guessing game
#TODO
# 1. First get random number from random package import random
# 2. Check the number is correct of not
# 3. Give user 5 chances

import random

random_number = random.randrange(1, 20, 1)


def math(user_value,random_value,count ,total_chances):
    if user_value==random_value:
        print(f"It matched the random decission {user_value}")
        return True
    else:
        print(f"{user_value}  doesn't matched please try again you have {total_chances - count} left:")
        return False

# math(user_value=user,random_value=random_number)  
count = 1
total_chances = 10
while count <= total_chances:
    user= int(input(f"Enter a random number "))
    terminate = math(user_value=user, random_value=random_number , count=count ,total_chances=total_chances)    
    if terminate == True:
        break
    else: 
        count = count + 1
        continue 

