
import random
import sys

sys.setrecursionlimit(10000)

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


def max_val(to_consider, avail):
    """Assumes to_consider a list of tiems, avail a weight.
    Returns a tuple of the totla value of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        #explore right branch only
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        #explore left branch
        with_val, with_to_take = max_val(to_consider[1:], avail - next_item.get_weight())
        with_val += next_item.get_value()
        #explore right branch
        without_val, without_to_take = max_val(to_consider[1:], avail)
        #choose better branche
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item, ))
        else:
            result = (without_val, without_to_take)
    return result

def fast_max_val(to_consider, avail, memo={}):
    """Assumes to_consider a list of items, avail a weight
    memo supplied by recursive calls.
    Returns a tuble of the total value of a solution to the
    0/1 knapsack problem and the items of that solution"""
    
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        #explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        #Explore left branch
        with_val, with_to_take = fast_max_val(to_consider[1:], avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()
        #Explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:], avail, memo)
        #Choose the better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item, ))
        else:
            result = (without_val, without_to_take)
            
    memo[(len(to_consider), avail)] = result
    return result

def small_test():
    names = ["a", "b", "c", "d"]
    vals = [6,7,8,9,]
    weights = [3,3,2,5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = max_val(Items, 5)
    for item in taken:
        print(item)
    print("Total value of itmes taken =", val)

def build_many_items(num_items, max_val, max_weight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i), random.randint(1, max_val), random.randint(1, max_weight)))
    return items

def big_test(num_items, avail_weight):
    items=build_many_items(num_items, 10, 10)
    val, taken = fast_max_val(items, 1000)
    print("Items Taken")
    for item in taken:
        print(item)
    print("Total value of items taken =", val)

#small_test()
big_test(1024,100)