def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1
    change is a positvie int,
    return the minimum number of coins needed to have a set of coints
    the values of which sum to change. Coins may be used more than once.
    For example, make_change([1,5,8],11) should return 3"""
    tab = [x for x in range(change + 1)]
    
    for i in range(change + 1):
        for coin in coin_vals[1:]:
            idx = i + coin
            new_val = tab[i] + 1
            if idx < len(tab):
                if new_val >= tab[i+coin]:
                    continue
                else:
                    tab[i+coin] = tab[i] + 1
            
    return tab[-1]

print(make_change([1,5,8], 2159478))

