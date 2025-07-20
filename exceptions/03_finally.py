def chimple():
  try:
    return True
  finally:
    return False

print(chimple())

def loop():
  for i in range(10):
    if i > 3:
      try:
        break
      finally:
        print("In finally")
    else:
      print(i)
  return None

loop()
