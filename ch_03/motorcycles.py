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
