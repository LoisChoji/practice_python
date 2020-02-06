def add(x, y *args, **kwargs):
    sum = x + y
    for a in args: 
        sum += a
