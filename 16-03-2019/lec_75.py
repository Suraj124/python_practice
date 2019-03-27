def display():
    def hello():
        return "Programming"
    return hello

fun=display()  #when one function return another function it return its address so we assign address to a variable
print(fun())   #now vraible is function with parenthesis