# Odd Number Triangle
# File: odd_number_triangle.py

# Question:

# 1
# 33
# 555
# 7777
# 99999


last_unused = 1

for row in range(1, 6):
    for numbers in range(last_unused, last_unused + 1):
        print(f'{numbers}' * row)
        last_unused += 2