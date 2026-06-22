# Pyramid Stars
# File: star_pyramid.py

# Question:

#     *
#    ***
#   *****
#  *******
# *********

star = 1

for row in range(1, 6):
    print(f'{' ' * (6 - row)}{'*' * star}')
    star += 2
