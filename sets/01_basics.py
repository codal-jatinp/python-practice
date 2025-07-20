basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

basket.add('apple')

print(basket, 'banana' in basket)

for x in basket:
  print(x)

a = set('abcdefg')
b = set('defg')

print (a - b)

print(b.intersection(a))

print(a > b)
# print(a + b)

print({ x for x in 'abracadabra' if x not in 'abc'})
