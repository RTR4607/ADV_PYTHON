def decor(func):
    def inner(name):
        if name=='hcl':
            print('hello hcl')
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name)
wish('python')