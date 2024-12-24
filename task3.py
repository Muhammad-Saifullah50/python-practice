# print factorial of a number

number = input('Enter a number \t')

if number.isnumeric():
    # calculating factorial
    usablenumber = int(number)

    factorial = 1

    for iterator in range(1, usablenumber + 1):
        factorial = factorial * iterator

    print('Factorial of ', usablenumber, 'is', factorial)
else :
    print("Invalid input")