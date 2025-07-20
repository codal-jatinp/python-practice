user = { 'id': 1, 'name': 'jatin', 'alias': 'Thors' }

keys = user.keys()
values = user.values()
items = user.items()
pair = zip(keys, values)

keys_len = len(keys)

print(*keys, keys_len)
print(*values)
print(*items)

user.setdefault('height', 5.3)

print(*keys, keys_len, len(user))
print(*values)
print(*items)

print(pair)
