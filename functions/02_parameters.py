# # Default Arguments

# def ask_ok(prompt, retries = 4, reminder = 'Please try again') -> bool: 
#   """Prompt user repeatadly

#   Args:
#       prompt (string): Prompt string
#       retries (int, optional): _description_. Defaults to 4.
#       reminder (str, optional): _description_. Defaults to 'Please try again'.

#   Returns:
#       bool: _description_
#   """
#   while True:
#     reply = input(prompt)
#     yes_values = ['y', 'ye', 'yes']
#     no_values = { 'n', 'no', 'nope' }
#     if reply in yes_values:
#       return True
#     if reply in no_values:
#       return False
#     retries -= 1

#     if retries < 0:
#       break
#     print(reminder)
  
#   print("Reply is still accessible", reply)
  
#   return ValueError("Invalid user response")


# ask_ok('OK to overwrite the file?')


# i = 5

# # Evaluated at time of function definition
# def f(arg = i):
#   print(arg)

# i = 6
# f()

# And default value is evaluated only once, so mutable objects are dangerous
def f(a, L = []):
  L.append(a)
  return L

print(f(1))
print(f(2))
print(f(3))

def f2(a, L = None) -> None:
  if L is None:
    L = []
  
  L.append(a)
  return L

print(f2(1))
print(f2(2))
print(f2(3))

