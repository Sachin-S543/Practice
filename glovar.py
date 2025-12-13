#when we create a variable inside a function it will be local means it can only accessed by in the function only if we want to create a global variable inside a function we can use global keyword to do that
def myfunc():
    global a
    a='hello'
    print(a)
myfunc()
print(a," world!")
