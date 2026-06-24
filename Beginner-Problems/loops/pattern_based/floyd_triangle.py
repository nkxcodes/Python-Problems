# Floyd's Triangle

# Print:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# File name: floyd_triangle.py

last_unused = 1

for row in range(1, 6):
    for number in range(last_unused, row + last_unused):
        last_unused += 1
        print(number, end = ' ')
    print('')