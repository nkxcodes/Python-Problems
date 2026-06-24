# Reverse Number Triangle

# Print:

# 12345
# 1234
# 123
# 12
# 1

# File name: reverse_number_triangle.py

for row in range(6, 1, -1):
    for number in range(1, row):
        print(number, end = '')
    print('')