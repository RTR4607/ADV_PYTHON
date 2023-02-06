def hello():
    print("hello function")
def call(func):
    temp=func()
    return temp
d=call(hello)
