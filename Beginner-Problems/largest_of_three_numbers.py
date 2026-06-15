# Largest of Three Numbers
# Same idea, but with 3 numbers.

first_number = int(input('Enter First Number: '))
second_number = int(input('Enter Second Number: '))
third_number = int(input('Enter Third Number: '))

if first_number >= second_number and first_number >= third_number:
    print(first_number)
elif second_number >= first_number and second_number >= third_number:
    print(second_number)
else:
    print(third_number)