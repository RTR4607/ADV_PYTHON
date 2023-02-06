old_price=[23,4,5,80,2,60,70,69,79,90,86]
rs=5
def add_price(old_price):
    return old_price+rs
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(list(new_price1))