import os
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy

path = "/home/barthk012/code/repo/mitx_python/finger_exercises/chapter19"
os.chdir(path)

def get_BM_data(filename):
    """REad the contents of the given file. Assumes the file is 
    in a comma-separated format, with 6 elements in each entry:
    0. Name (string), 1. Gender (string) 2. Age(int), 
    3. Division (int), 4. Country (string), 5. Overall time (float)
    returns a dictionary containing a list for each of the 6 variables"""

    data = {}
    with open(filename, "r") as f:
        f.readline() # discard first line (with the labels)
        line = f.readline()
        for k in ["name", "gender", "age", "division", "country", "time"]:
            data[k] = []
        while line != "":
            split = line.split(",")
            data["name"].append(split[0])
            data["gender"].append(split[1])
            data["age"].append(split[2])
            data["division"].append(split[3])
            data["country"].append(split[4])
            data["time"].append(float(split[5][:-1])) #remove the \n
            line = f.readline()
        return data

def sample_times(times, num_examples):
    """Assumes times is a list of floats representing finishing times
    fo all runners, num_examples is an int
    Generates a random sample of size num_examples, and produces a histogram showing
    the distribution alaong with its mean and standard deviation"""
    sample = random.sample(times, num_examples)
    print("Length of Sample = ", len(sample))
    make_hist(sample, 10, f"Sample of Size {num_examples}", "Minutes to complete Race", "Number of runners", "sample.jpg")

def make_hist(data, bins, title, x_label, y_label, filename):
    plt.hist(data, bins)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    mean = sum(data) / len(data)
    std = np.std(data)
    plt.annotate(f"Mean = {round(mean, 2)}\nSD = {round(std, 2)}", 
                fontsize=14, xy = (0.65, 0.75), xycoords = "axes fraction")
    plt.savefig(filename)
    plt.clf()

def gaussian(x, mu, sigma):
    factor1 = (1/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-((x-mu)**2/(2*sigma**2))
    return factor1 * factor2


times = get_BM_data("bm_results2012.csv")["time"]
make_hist(times, 20, "2012 Boston Marathon", "Minutes to complete race", "Number of Runners", "pop.jpg")
sample_size = 40
sample_times(times, sample_size)