def merge(left, right, compare):
    """assumes left and right are sorted lists and
    compare defines an ordering of the elements(lambda function e.g.)
    Returns a new sorted (by compare) list containing the same
    elements as (left + right) would contain"""

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while (i < len(left)):
        result.append(left[i])
        i+=1
    while (j < len(right)):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L, compare = lambda x, y: x < y):
    """Assumes L is a list compare deifens an ordering
    on elements of L
    Returns a new sorted list with the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

L = [2, 1,4,5,3]
print(merge_sort(L), merge_sort(L, lambda x, y: x > y))

#fingex
L = [(5,2), (1,8), (1,2,3)]
print(merge_sort(L, lambda x, y: sum(x) < sum(y)))
