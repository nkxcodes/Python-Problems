# Count Even Numbers
#
# Create a program that counts how many even numbers
# are present in a list
#
# Requirements:
# - Create a list of integers.
# - Use a for loop to go through each number.
# - Use an if statement to check whether the number is even.
# - Coutn the total number of even numbers.
# - Print the final count 
# 
# Example:
# Numbers: [3, 8, 5, 12, 7, 10, 1]
# Output: 
# There Are 3 Even Numbers.

numbers = [3, 8, 5, 12, 7, 10, 1]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1


print(f'There Are {count} Even Numbers.')