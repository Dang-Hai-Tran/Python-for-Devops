# Syntax: lambda <param>: <return expression>

num = lambda i: i**2
print(num(5))

items = [(0, 'a', 2), (5, 'b', 0), (2, 'c', 1)]
print(sorted(items, key= lambda tuple: tuple[2]))
