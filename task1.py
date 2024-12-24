# Generate a random number from 3 to 13

import random

generate = 'y'

while generate == 'y' :
  number = random.randint(3,13)
  print(number)

  prompt = input("Do you want to continue ?? Enter y / n \t")

  match prompt: 
    case 'y':
      generate = prompt

    case 'n': 
      generate = 'n'
      print('Thanks for using ')

    case _: 
      print("Invalid option")
 
  