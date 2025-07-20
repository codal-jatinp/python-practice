# LEGB: Local, Enclosing, Global, BuiltIn

name = 'jatin'

def log_global():
  print(name)

def log_local():
  name = 'Putin'
  hehe = 'haha'
  print(name)

def update_global():
  global name
  name = 'putin'
  print(name)

log_global()

log_local()

print(name)

update_global()

print(name)

print(update_global.__code__.co_varnames)