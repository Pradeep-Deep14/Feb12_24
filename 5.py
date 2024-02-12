def outer_function():
    x=5
    def inner_function():
        x=2
        x+=2

    inner_function()
    print(x)

outer_function()