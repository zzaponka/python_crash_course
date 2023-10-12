print('Initial list:')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print('\nChanging first element:')
motorcycles[0] = 'ducati'
print(motorcycles)

print('\nAdding element at the end:')
motorcycles.append('kawasaki')
print(motorcycles)

print('\nCleaning list:')
motorcycles = []
print(motorcycles)

print('\nAdding elements one by one:')
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print('\nInserting an element:')
motorcycles.insert(0, 'ducati')
print(motorcycles)

print('\nDeleting an element:')
del motorcycles[0]
print(motorcycles)

print('\nDeleting the element in the middle of the list:')
del motorcycles[1]
print(motorcycles)

print('\nUsing popped element:')
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f'Popped element: {popped_motorcycle}')

print('\nInitial list back:')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print('\nPopping element by index:')
second_moto = motorcycles.pop(1)
print(motorcycles)
print(f'Popped element: {second_moto}')

print('\nInitial list back again:')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print('\nRemoving element by value:')
motorcycles.remove('yamaha')
print(motorcycles)
