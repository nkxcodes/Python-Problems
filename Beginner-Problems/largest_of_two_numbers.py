# Largest of Two Numbers
# Take two numbers and print which one is bigger.

first_number = int(input('Enter First Number: '))
second_number = int(input('Enter Second Number: '))

if first_number > second_number:
    print(first_number)
elif second_number > first_number:
    print(second_number)
else:
    print('Both Are Equal')