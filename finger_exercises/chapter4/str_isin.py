def isin(s1, s2):
    """returns True if either string occurs anywhere in the other, Fals otherwise"""
    if (s1 in s2) or (s2 in s1):
        return True
    else:
        return False
    
def test_isin(strings1, strings2):
    for s1 in strings1:
        for s2 in strings2:
            res = isin(s1,s2)
            if res == True:
                print(f"{s1} in {s2} or vice versa")
            else:
                print(f"{s1} not in {s2} or vice versa")
                
                
strings1 = ["hello", "world", "doof", "name", "test"]
strings2 = ["bwahellola", "nahworldina", "of", "ame", "twintesting"]

test_isin(strings1, strings2)