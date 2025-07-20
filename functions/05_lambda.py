# def make_incrementor(n):
#   return lambda x: x + n

# f = make_incrementor(2)

# print(f(1))
# print(f(2))

# sum = lambda x,y: x + y

# print(sum(1, 2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three')]

pairs.sort(key=lambda pair: pair[1])

print(pairs)
