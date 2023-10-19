pizzas = ['napoletana', 'margherita', 'marinara']
friend_pizzas = pizzas[:]

pizzas.append('calzone')
friend_pizzas.append('pepperoni')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza.title())
