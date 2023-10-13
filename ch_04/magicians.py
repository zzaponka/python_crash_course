magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print('\nPersonalized messages:')
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
