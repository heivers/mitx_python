def get_min(d):
    """d a adict mapping letters to ints
    returns the value in d with the key that occurs first 
    in the alphabet"""
    return d[sorted(d.keys())[0]]

d = {"x": 11, "b": 12}

print(get_min(d))