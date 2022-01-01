"""accepts either one or two ints as arguments. If called with two,
function prints the product, else the argument"""

def mult(x, y=False):
    if y == False:
        return(x)
    else:
        return (x*y)
    
print(mult(5))
print(mult(10,6))
print(mult(3,2))