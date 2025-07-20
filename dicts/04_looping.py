# for i, v in enumerate([1, 2, 3, 'hehe' ]):
#   print(i, v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['John', 'holy grail', 'blue']


# for q, a in zip(questions, answers):
#   print('What is your {0}? It is {1}.'.format(q, a))

print(*filter(lambda x: x > 2, [1,2,3,4,5]))

def gt_two(x:int) -> bool:
  print('invoked')
  return x > 2

result_itr = filter(gt_two, [10,1,2,3,4,5]) # Is lazily evaluated

print('about to print result')
print(*result_itr)
