name: str = 'python'

print(name[0])
print(name[-1])

index = slice(0, 3)
print(name[index])

print(name[3:]); #Elements from index 3
print(name[:3]) #Elements till index 3
print(name[-1:]) #last element
print(name[::2]) #Every second element
print(name[1::2]) #Every second element

print(name[:2] + name[2:])

print(len(name))