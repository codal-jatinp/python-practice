def cheeseshop(kind, *args, **kwargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in args:
      print(arg)
    
    for kw in kwargs:
      print(kw , " : ", kwargs[kw])

cheeseshop('Limburger', "It's very runny, sir.", "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def pos_only(arg0, /) -> None:
  print(arg0)

pos_only(1)
# pos_only(1, 2)

def kw_only(*, args) -> None:
  print(args)

kw_only(args= 'jatin')
# kw_only(** { 'args': 2, 'name': 'jatin' })

def combined_example(pos_only: int, /, standard: int, *, kw_only) -> None:
  print(pos_only, standard, kw_only, sep=' / ')

print(combined_example.__annotations__)

combined_example(1, kw_only = 'jatin', standard= 2)
