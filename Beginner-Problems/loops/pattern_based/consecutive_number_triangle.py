# Consecutive Number Triangle
# File: consecutive_number_triangle.py

# Question:

# 1
# 23
# 456
# 78910

last_unused = 1

for rows in range(1, 5):
    for number in range(1, 2):
        for numbers in range(last_unused, rows + last_unused):
            print(numbers, end = '')
            last_unused += 1
        print('')