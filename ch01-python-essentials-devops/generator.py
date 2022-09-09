def fibo():
    first = 0
    last = 1
    while True:
        yield first
        first, last = last, first + last

fi = fibo()
for i in fi:
    if i < 100:
        print(i, end=',')
    else:
        break

def even_or_odd():
    var = True
    while True:
        if var == True:
            yield "Even"
        else:
            yield "Odd"
        var = not var

generator_even_odd = even_or_odd()
count = 1
while count < 10:
    print(next(generator_even_odd))
    count += 1
