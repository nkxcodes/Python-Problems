# Print factorial of a number using a loop.

entered_number = int(input("Enter A Number: "))

output = 1

for numbers in range(entered_number, 0, -1):
    output *= numbers

print(output)