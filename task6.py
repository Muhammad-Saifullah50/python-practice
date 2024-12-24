# print factorial of 3 numbers

number1 = input('Enter first number \t')
number2 = input('Enter second number \t')
number3 = input('Enter third number \t')

if (number1.isnumeric() and number2.isnumeric() and number3.isnumeric()):
    # calculating factorial
    usablenumber1 = int(number1)
    usablenumber2 = int(number2)
    usablenumber3 = int(number3)

    factorial_num_1 = 1
    factorial_num_2 = 1
    factorial_num_3 = 1
    

    for iterator in range(1, usablenumber1 + 1):
        factorial_num_1 = factorial_num_1 * iterator

    print('Factorial of ', usablenumber1, 'is', factorial_num_1)
    
    for iterator in range(1, usablenumber2 + 1):
        factorial_num_2 = factorial_num_2 * iterator

    print('Factorial of ', usablenumber2, 'is', factorial_num_2)
    
    for iterator in range(1, usablenumber3 + 1):
        factorial_num_3 = factorial_num_3 * iterator

    print('Factorial of ', usablenumber3, 'is', factorial_num_3)
else :
    print("Invalid input")