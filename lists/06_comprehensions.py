from math import pi

squares = []

for x in range(5):
  squares.append(x ** 2)

print(squares, x)

squares = list(map(lambda y: y ** 2, range(5)))

print(squares, x)

squares = [x** 2 for x in range(5) if x > 1]

print(squares)

print([(x, y) for x in range(4) for y in range(4) if x != y])

print([str(round(pi, i)) for i in range(5)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(len(matrix))])

print(list(zip(*matrix)))