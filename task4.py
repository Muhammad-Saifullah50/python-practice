# print table of a number 

table_number = input('Enter the number which you want the table for \t')
limit = input('Enter the limit of the table \t')

if (table_number.isnumeric() and limit.isnumeric()):
    
    usable_table_number = int(table_number)
    usable_limit = int(limit)

    for iterator in range(1, usable_limit+1):
        print(usable_table_number, 'x', iterator, '=', usable_table_number * iterator)
else: 
    print('Invalid input')