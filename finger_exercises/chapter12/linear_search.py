def lin_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

def lin_search_ordered(L,e):
    """Assumes L is a list, the elements of which are in 
    ascending order"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search(L, e):
    """Assumes L is a list, the elements of which are in 
    aschending order.
    Returns True if e is in L and False otherwise"""

    def bin_search(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bin_search(L, e, low, mid-1)
        else:
            return bin_search(L, e, mid+1, high)

    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)

#print(lin_search([1,2,3,4,5,6,"A", "a"], "b "))

print(search([1,2,3,4,6,7,8,9,10], 1 ))