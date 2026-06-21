# Right-Aligned Numbers
# File: right_aligned_numbers.py

# Question:

#     1
#    12
#   123
#  1234
# 12345

total = ''

for numbers in range(1, 6):
    total += f'{numbers}'
    print(f'{' ' * (6 - numbers)}{total}')