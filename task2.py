# Generate  random odd number from 10 to 100  and even numbers from 200 to 96

import random

generate = 'y'

while generate == 'y' :
  first_number = random.randint(10,100)
  second_number = random.randint(96,200)

  if (first_number % 2 != 0): 
    odd_number = first_number

  if (second_number % 2 == 0): 
    even_number = second_number 

  print("The generated odd number ", odd_number)
  print("The generated even number ", even_number)

  prompt = input("Do you want to continue ?? Enter y/n \t")

  match prompt: 
    case 'y':
      generate = prompt

    case 'n': 
      generate = 'n'
      print('Thanks for using ')

    case _: 
      print("Invalid option")
 