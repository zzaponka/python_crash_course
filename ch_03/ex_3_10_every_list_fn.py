things = ['battery', 'headlight', 'tracker', 'soldering', 'lamp', 'cable']
print('Things on my table:')
print(things)
print(f'\nFirst element: {things[0]}')
print(f'Second element: {things[1]}')
print(f'Title format: {things[0].title()}')
print(f'Last element: {things[-1]}')
things[0] = 'jack'
print('\nFirst element has been changed:')
print(things)
print('\nAdding element at the end:')
things.append('headphones')
print(things)
print('\nInserting element at the beginning:')
things.insert(0, 'scissors')
print(things)
print('\nRemoving second element, there\'s no more jack...')
del things[1]
print(things)
print('\nRemoving with pop() from the end of the list:')
removed = things.pop()
print(things)
print(f'And removed element: {removed}')
print('\nRemoving with pop() by index (should be \'tracker\'):')
removed = things.pop(2)
print(things)
print(f'Removed element: {removed}')
print('\nRemoving by value (should be no \'soldering\' by now):')
things.remove('soldering')
print(things)
print('\nRemoving with variable\'s value (should be no \'lamp\' by now):')
removed = 'lamp'
things.remove(removed)
print(things)
print('\nTemporarily sorting:')
print(sorted(things))
print('The list is still in its original state:')
print(things)
print('\nSorting permanently:')
things.sort()
print(things)
print('And in reverse order:')
things.sort(reverse = True)
print(things)
print(f'\nFinal length of the list: {len(things)}')
