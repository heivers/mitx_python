import random
import numpy as np

"""
The chance of rolling a 6 = 1/6
The chance of also rolling two 6's = (1/6)**2 -> 1/36
That means the chance of not rolling a double 6 on the first roll = 1- 1/36 = 35/36
That means the chance of not rolling a double 6 in 24 rolls = (35/36)**24 = 0.508596
That means chance of rolling a double 6 in 24 rolls is 1- 0.508596
"""

def roll_die():
    return random.choice(range(1,7))

def check_pascal(num_trials):
    """Assumes num_trials is an int > 0
    Prints an estimate of the probabilty of winning"""
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print(f"Probability of winning = {num_wins/num_trials:.3f}")

check_pascal(100000)
print(f"Official result = {round(1 - (35/36)**24,3)}")