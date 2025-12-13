#golbal variable is when a variable created outside function and it can be accessed from inside and outside of the function
x="world"
def myfunc():
    print("hello ",x)
myfunc()