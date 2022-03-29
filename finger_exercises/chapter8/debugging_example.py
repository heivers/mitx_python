def is_pal(x):
    """Assumes x is a list
    Returns True if the list is a palindrome, False otherwise"""
    temp = x[:]
    temp.reverse()
    print(temp, x)
    return temp == x

def silly(n):
    """Assumes n is an int > 0
    Gets n inputs from the user
    Print 'Yes' if the sequence of inputs forms a palindrome,
    'No' otherwise """
    result = []
    for i in range(n):
        #result = [] wrongfully placed here(2)
        elem = input("Enter element: ")
        result.append(elem)
    print(result) #debug print (1)
    if is_pal(result):
        print("Yes")
    else:
        print("No")

silly(2)