# words = ['cat', 'dog', 'stitch']

# for w in words:
#   print(w)

# items = {'Hans': 'active', 'elenor': 'inactive' }

# for user,status in items.items():
#   print(user, status)

# for i in range(5):
#   print(i)

# for i in range(len(words)):
#   print(i, words[i])

for i in range(10):
    if i % 2 == 0:
      continue
    if i % 30 == 0:
      print("Breaking apart")
      break
    print(i)
else:
    print('got in else', i)