# Hollow Square
# File: hollow_square.py

# Question:

# *****
# *   *
# *   *
# *   *
# *****

# Solution - 1

for rows in range(1, 6):
    if rows == 2 or rows == 3 or rows == 4:
        print('*   *')
    elif rows == 1 or 5:
        print('*' * 5)