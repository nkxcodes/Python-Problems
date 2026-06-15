# Simple Calculator
# Take:
# 2 numbers
# an operator (+, -, *, /)
# Perform the operation.


first_number = int(input('Enter First Number: '))
second_number = int(input('Enter Second Number: '))
operator = input('Enter A Operator(Default+): ')

if operator == '+' or operator == '':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == '/':
    if second_number == 0:
        print('Cannot Divide By Zero!')
    else:
        print(first_number / second_number)
else:
    print('Invalid Operator!')