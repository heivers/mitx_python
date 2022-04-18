def sel_sort(L):
    """Assumes that L is a list of elements that can be compared
    using >
    Sorts L in ascending order"""
    suffix_start = 0
    while suffix_start != len(L):
        #look at each element in the suffix
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                #swap position
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start +=1

    return L

print(sel_sort([4,3,7,2,1,8,9,12,11]))

    
