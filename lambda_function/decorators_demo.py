def outer():
    print("Hello outer function")
    def inner():
        print("Hello inner function")
        def inner1():
                print("Hello inner1")
        return inner1
    return inner

outer()()()
