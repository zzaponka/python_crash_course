print('Create a list of squares from 1 to 10 with temprary variable:')
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

print('\nAnd without temprary variable:')
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
