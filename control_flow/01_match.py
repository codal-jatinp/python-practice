name = input("What you're doing next?: ")

a = 'action'
b = 'send_mail'

match name.split(" "):
  case "quite":
    quit()
  case ["go", "north" | "south"]:
    print(f"Going {name.split(' ')[-1]}")
  case ["north"] | ["go", "north"]:
    print("going north")
  case _:
    print("default action")