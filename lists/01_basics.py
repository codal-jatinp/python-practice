squares = [1,2,3,4,5]

print(squares + [6, 7])

print(squares * 3)
print([item ** 3 for item in squares ])

print(id(squares))
squares.append(-1)

print(id(squares))

# Remove elements
squares[1:2] = []

print(squares)