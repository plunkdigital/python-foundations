print('Enter tree size')
size = int(input('>'))
row_num = 1
while row_num < size + 1:
    print(' ' * (size - row_num) + '^' * (row_num *2 -1))
    row_num = row_num + 1
print(' ' * (size - 1) + '#')
print(' ' * (size - 1) + '#')
