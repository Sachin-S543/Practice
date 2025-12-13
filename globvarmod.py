#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x="hi"
print("Before function call:",x)
def myfunc():
    global x
    x="Hello"
    print("Inside function:",x)
myfunc()