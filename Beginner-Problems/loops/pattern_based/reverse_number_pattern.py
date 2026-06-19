# Reverse Number Pattern
# File: reverse_number_pattern.py

# Question:

# 54321
# 5432
# 543
# 54
# 5

for number in range(1, 6):
    for digit in range(5, number - 1, -1):
        print(digit, end = '')

    print('')