import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def roll_n(n):
    result = ""
    for i in range(n):
        result += str(roll_die())
    print(result)

#roll_n(10)

def flip(num_flips):
    """Assumes num_flips is a postivive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(("H", "T")) == "H":
            heads += 1
    return heads / num_flips

def flip_sim(num_flips_per_trial, num_trials):
    """Assumes num_flips_per_trial and num_trials positive ints"""
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads) / len(frac_heads)
    return mean

#print(flip_sim(100, 100000))

def regress_to_mean(num_flips, num_trials):
    #Get Fraction of heads for each trail of num_flips
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    #find trials with extreme result an for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i + 1])
    #Plot results
    plt.plot(range(len(extremes)), extremes, "ro", label="Extreme")
    plt.plot(range(len(next_trials)), next_trials, "b^", label="Next Trial")
    plt.axhline(0.5)
    plt.xlim(-1, len(extremes) + 1)
    plt.ylim(0, 1)
    plt.xlabel("Extreme example and next trial")
    plt.ylabel("Fraction Heads")
    plt.title("Regression to Mean")
    plt.legend(loc="best")
    plt.savefig("Reg_mean.jpg")

def flip_plot(min_exp, max_exp):
    """Assumes min_exp and max_exp positive ints, min_exp < max_exp
    Plots results of 2**min_exp to 2**max_exp coin flips"""
    ratios, diffs, xAxis = [], [], []
    for exp in range(min_exp, max_exp +1):
        xAxis.append(2**exp)
    for num_flips in xAxis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(("H", "T")) == "H":
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads-num_tails))
        except ZeroDivisionError:
            continue
    plt.title("Differnce Between Heads and Tails")
    plt.xlabel("Number of flips")
    plt.ylabel("Abs(#Heads-#Tails)")
    plt.xticks(rotation="vertical")
    plt.semilogx()
    plt.semilogy()
    plt.plot(xAxis, diffs, "ko")
    plt.savefig("Difference.jpg")
    plt.figure()
    plt.title("Heads/Tails Ratios")
    plt.xlabel("Number of Flips")
    plt.ylabel("#Heads/#Tails")
    plt.xticks(rotation="vertical")
    plt.semilogx()
    plt.plot(xAxis, ratios, "ko")
    plt.savefig("Ratios.jpg")


def variance(X):
    """Assumes taht X is a list of numbers.
    Returns the variance of X"""
    mean = sum(X) / len(X)
    tot = 0
    for x in X:
        tot += (x-mean)**2
    return tot / len(X)

def std_dev(X):
    """Assumes that X is a list of numbers.
    Retunrs the standard deviation of X"""
    return variance(X)**0.5

#regress_to_mean(10, 50)
random.seed(0)
flip_plot(4, 20)