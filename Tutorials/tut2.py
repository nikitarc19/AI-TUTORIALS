# Create a scisor paper and rock game.
# Winning condition (computer = S, user = R), (computer = R, user = P), (computer = P, user = S)
# Draw comuter = user


import random

computer_guessing = random.choice(['s','r','p'])
  
def choose(user_choice,computer_guessing):
  
  if user_choice!='r' and user_choice!='s' and user_choice!= 'p':
    print(f"Wrong Input")
  elif user_choice==computer_guessing:
    print(f"Match is draw ")
  elif (computer_guessing=='s' and user_choice=='r') or(computer_guessing=='r' and user_choice=='p') or(computer_guessing=='p' and user_choice=='s'):
     print(f"User win the match ")
  else:
    print(f'You Lose!')
  
count = 1
total_chances = 5
while count <= total_chances:
    user_choice = input('Enter the value "r", "s", "p":')
    choose(user_choice,computer_guessing)
    count = count +1







