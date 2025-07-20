from collections import namedtuple

items = list(range(4))

tupled = tuple(items)

print(items, tupled)

tupled = ((1, 2), (3, 4))

print(tupled, [*tupled[0], *tupled[1]])

tupled = 1,2, 3, 4, 5

print(tupled)

empty = ()
singleton = 'hello',

print(empty, singleton, len(singleton))

print((1, 2) + (3, 4))

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, y = 2)

y, x = p

print(x, y)

Point3D = namedtuple('Point3D', Point._fields + ('z',), defaults=[0,0,0])

print(Point3D())

print(getattr(Point3D(1,2,3), 'z'))

