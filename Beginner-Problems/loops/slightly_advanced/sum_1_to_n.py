# Find the sum of numbers from 1 to N (take N from user).

entered_number = int(input('Enter A Number: '))
total = 0

for numbers in range(1, entered_number+1):
    total += numbers
    print(numbers)

print(f"Total: {total}")