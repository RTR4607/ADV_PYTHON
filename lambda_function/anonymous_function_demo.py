def demo(x):
    return lambda a:a*x
demo=demo(2)
print(demo(5))