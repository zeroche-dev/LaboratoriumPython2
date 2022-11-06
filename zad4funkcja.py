def sqfunc(x):
    return (2 * pow(x, 2)) - (5 * x) - 8

start = -4
end = 4

while start <= end:
    y = sqfunc(start)
    print(f"for x: {start} y is : {y}")
    start += 0.5

