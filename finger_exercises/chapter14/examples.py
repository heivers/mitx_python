from itertools import combinations, chain

"""Knapsack problem - Greedy"""
class Item():
    def __init__(self, name, value, weight):
        self._name = name
        self._value = value
        self._weight = weight

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight
        
    def __str__(self):
        return f"<{self._name},    {self._value},    {self._weight}>"

def value(item):
    return item.get_value()

def weight_inverse(item):
    return 1.0 / item.get_weight()

def density(item):
    return item.get_value() / item.get_weight()


def greedy(items, max_weight, key_function):
    """Assumes items is a list, max_weight >= 0, 
    key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight() <= max_weight):
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)

def build_items():
    names = ["clock", "painting", "radio", "vase", "book", "computer"]
    values = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    items = []
    for i in range(len(names)):
        items.append(Item(names[i], values[i], weights[i]))

    return items

def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print("Total value of items taken is", val)
    for item in taken:
        print("    ", item)

def test_greedys(max_weight = 20):
    items = build_items()
    print("Use greedy by value to fill knapsack of size", max_weight)
    test_greedy(items, max_weight, value)
    print("Use greedy by weight to fill knapsack of siez", max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print("Use greedy by densitey to fill knapsack of size", max_weight)
    test_greedy(items, max_weight, density)

test_greedys()

def powerset(items):
    s = list(items)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = None
    for items in pset:
        items_val = 0.0
        items_weight = 0.0
        for item in items:
            items_val += get_val(item)
            items_weight += get_weight(item)
        if items_weight <= max_weight and items_val > best_val:
            best_val = items_val
            best_set = items
    return (best_set, best_val)

def test_best(max_weight=20):
    items = build_items()
    pset = powerset(items)
    taken, val = choose_best(pset, max_weight, Item.get_value, Item.get_weight)
    print("Total value of items taken is", val)
    for item in taken:
        print(item)
        
test_best() 