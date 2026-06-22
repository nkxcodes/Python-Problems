# Number Pyramid
# File: number_pyramid.py

# Question:

#     1
#    121
#   12321
#  1234321
# 123454321


total_1 = ''
total_2 = ''

for row in range(1, 6):
    total_1 += f'{row}'
    if row >= 2:
        for num in range(row - 1, row):
            total_2 = f'{num}' + total_2
    print(f'{' ' * (6 - row)}{total_1 + total_2}')

