# A nested function is a function defined inside another function.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
#inner() NameError: name 'inner' is not defined. Did you mean: 'iter'?
outer()
