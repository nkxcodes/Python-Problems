# Count how many numbers between 1 to N are divisible by 3.

n_number = int(input('Enter A Number: '))
total = []

for numbers in range(1, n_number+1):
    if numbers % 3 == 0:
        print(numbers)
        total.append(numbers)

print(f"Total: {len(total)}")