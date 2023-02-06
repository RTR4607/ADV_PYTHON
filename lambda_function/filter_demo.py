li=[23,4,5,80,2,60,70,69,79,90,86]
def demo_fun(n):
    if n>=80:
        return True
    else:
        return False
data=list(filter(demo_fun,li))
print(data)