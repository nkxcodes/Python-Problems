# Odd Number Triangle
# File: odd_number_triangle.py

# Question:

# 1
# 33
# 555
# 7777
# 99999

for rows in range(1, 6):
    for number in range(1, 2):
        for numbers in range(1, 10, 2):
            if numbers % 3 == 0:
                print(f'{numbers}' * rows)