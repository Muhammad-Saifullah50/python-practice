# Take two values and tell the highest and lowest value

generate = 'y'

while generate == 'y':
    number1 = input('Enter first number \t')
    number2 = input('Enter second number \t')

    if number1.isnumeric() and number2.isnumeric():
        number1 = int(number1)
        number2 = int(number2)
        
        if number1 > number2:
            highest_number = number1
            lowest_number = number2
        elif number1 < number2:
            highest_number = number2
            lowest_number = number1
        else:
            print('Both numbers are equal')
            highest_number = number1
            lowest_number = number2

        print("Highest number is", highest_number)
        print("Lowest number is", lowest_number)
    else:
        print("Invalid input. Please enter numeric values.")

    prompt = input("Do you want to continue? Enter y/n \t")

    match prompt:
        case 'y':
            generate = prompt
        case 'n':
            generate = 'n'
            print('Thanks for using')
        case _:
            print("Invalid option")
