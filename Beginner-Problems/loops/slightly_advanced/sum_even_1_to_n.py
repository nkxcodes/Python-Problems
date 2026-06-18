# Print the sum of all even numbers between 1 to N.

n_number = int(input("Enter A Number: "))

total = 0

for numbers in range(1, n_number+1):
    if numbers % 2 == 0:
        print(numbers)
        total += numbers

print(f"Total: {total}")