# Print a triangle pattern using alphabet letters

# Output:
# A
# AB
# ABC
# ABCD
# ABCDE

# Think:
# How can you convert numbers to letters?
# What changes in each row

alphabets = ['A', 'B', 'C', 'D', 'E']

total_alphabets = ''

for row in range(0, 5):
    total_alphabets += f'{alphabets[row]}'
    print(total_alphabets)