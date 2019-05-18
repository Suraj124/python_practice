def display():
    def hello():
        return "Programming"
    return hello

fun=display()  #when one function return another function it return its address so we assign address 
print(fun())   # to a variable now variable is function with parenthesis