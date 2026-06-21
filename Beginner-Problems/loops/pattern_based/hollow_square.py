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

# Solution - 2

for rows in range(1, 2):
    print('*' * 5)
    for int_rows in range(1, 4):
        print('*   *')
    print('*' * 5)