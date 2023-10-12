guests = ['Gandalf', 'Bilbo', 'Frodo']

print(f'Hi, dear {guests[0]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[1]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[2]}, I would like to invite you to the dinner!')

print(f'\nOops, it seems that {guests[1]} cannot make it...')
guests[1] = 'Sam'
print(f'Will call {guests[1]} instead.')

print(f'\nHi, dear {guests[0]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[1]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[2]}, I would like to invite you to the dinner!')
