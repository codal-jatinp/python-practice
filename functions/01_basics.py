wasSomething = False

def fib(n: int) -> None:
  """Prints a Fib less than n.

  Args:
      n (int): void
  """
  result = []

  global wasSomething
  wasSomething = True

  a, b = 0, 1



  while a < n:
    a, b = b, a + b
    result.append(a)

  return result

print(fib(10))

print(wasSomething)