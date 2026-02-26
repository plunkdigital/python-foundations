import random
print('Enter the tree size')
size = int(input('>'))
for row_num in range(1, size + 1):
    spaces = size - row_num
    branches = row_num * 2 - 1

    row = ' ' * spaces

    for _ in range(branches):
        if random.randint(1,4) == 1:
            row += 'o'
        else:
            row += '^'

    print(row)
trunk_spaces = size - 1
for _ in range(2):
    print(' ' * trunk_spaces + '#')

