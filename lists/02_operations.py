names = ['sandy', 'andy', 'thorfin', 'enel']
print(*names)

names.extend(['luffy'])

print(*names)

names.insert(0, 'God D. Ussop')

print(*names)

names.insert(-1, 'SaDBo')

print('index', names.index('SaDBo', 0, -1))

names.insert(len(names), "ACE")

print(*names)

names.remove('sandy')

print(*names)

print('luffy: ', names.count('luffy'))

names.reverse()

print(*names)

list.sort(names, reverse=False)

del names[:]

print(names)

