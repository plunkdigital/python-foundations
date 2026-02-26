print('Enter the tree size')
size = int(input('>'))
for row_num in range(1, size + 1):
    print(' ' * (size - row_num) + '^' * (row_num *2 -1))
print(' ' * (size - 1) + '#')
print(' ' * (size - 1) + '#')
