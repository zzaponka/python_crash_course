my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favourite foods are:')
for my_food in my_foods:
    print(my_food)

print('\nMy friend\'s favourite foods are:')
for friend_food in friend_foods:
    print(friend_food)
