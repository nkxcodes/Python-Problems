# Right-Aligned Stars
# File: right_aligned_stars.py

# Question:

#     *
#    **
#   ***
#  ****
# *****


for stars in range(1, 6):
    print(f'{' ' * (5 - stars)}{'*' * stars}')