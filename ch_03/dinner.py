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

print('\nOh, we have a new table, so can to invite more!')
guests.insert(0, 'Thorin')
guests.insert(2, 'Fili')
guests.append('Kili')

print(f'Hi, dear {guests[0]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[1]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[2]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[3]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[4]}, I would like to invite you to the dinner!')
print(f'Hi, dear {guests[5]}, I would like to invite you to the dinner!')
