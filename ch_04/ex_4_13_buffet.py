foods = ('burger', 'cake', 'sandwich', 'croissant', 'ice cream')
print('Original menu:')
for food in foods:
    print(food.title())

# Traceback (most recent call last):
#   File "/home/sshydlovskyi/src/pytnon/mapathon/./ch_04/ex_4_13_buffet.py", line 5, in <module>
#     foods[0] = 'soup'
# TypeError: 'tuple' object does not support item assignment
# foods[0] = 'soup'

foods = ('burger', 'cake', 'sandwich', 'soup', 'fried eggs')
print('\nRevised menu:')
for food in foods:
    print(food.title())
