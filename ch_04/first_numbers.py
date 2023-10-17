print('range() function stops one step before the upper limit, e.g. range(1, 5) prints:')
for value in range(1, 5):
    print(value)

print()
print('If you need elements from 1 to 5, you need to use range(1, 6):')
for value in range(1, 6):
    print(value)

print()
print('If you set only one argument, like range(6), it starts from zero:')
for value in range(6):
    print(value)
