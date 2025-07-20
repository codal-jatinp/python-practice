name = 'Jatin'

def outer_fn():
  global name

  name = 'Putin'
  id = None
  position = None

  def inner_fn():
    global id
    id = 1

    nonlocal position
    position = 'CEO'
    print('inner fn', name, id, position)
  
  inner_fn()
  print('outer fn', name, id, position)

outer_fn()

print('global', name, id)
