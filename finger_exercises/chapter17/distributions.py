import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import numpy as np

""" random.seed(42)
vals = [random.choice(range(101)) + random.choice(range(101)) for i in range(1000)]
print(len(vals))
plt.hist(vals, bins=10, ec= "k")
plt.xlabel("Sum")
plt.ylabel("Number of occurences")
plt.savefig("vals_dist.jpg") """

def flip(num_flips):
    heads = sum([random.choice((1,0)) for x in range(num_flips)]) 
    return heads / num_flips

def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = [flip(num_flips_per_trial) for x in range(num_trials)]
    return (frac_heads, np.mean(frac_heads), np.std(frac_heads))

def label_plot(num_flips, num_trials, mean, sd):
    plt.title(f"{num_trials} trials of {num_flips} flips each.")
    plt.xlabel("Fraction of Heads")
    plt.ylabel("Number of trials")
    plt.annotate(f"Mean = {mean:.4f}\nSD = {sd:.4f}", size="x-large", xycoords="axes fraction", xy = (0.67, 0.5))

def make_plots(num_flips1, num_flips2, num_trials):
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    plt.hist(val1, bins=20)
    label_plot(num_flips1, num_trials, mean1, sd1)
    fname = "first_dist.jpg"
    plt.savefig(fname)
    plt.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    plt.hist(val2, bins=20)
    label_plot(num_flips2, num_trials, mean2, sd2)
    fname = "second_dist.jpg"
    plt.savefig(fname)


make_plots(100, 1000, 100000)