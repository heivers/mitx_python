import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.inspection import plot_partial_dependence

# This changes the running directory to the directory where the py file is located.
os.chdir((sys.path)[0])

def get_data(input_file):
    with open(input_file, "r") as f:
        distances = []
        masses = []
        f.readline()
        for line in f:
            d, m = line.split(",")
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)

def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances[:-6])
    forces = np.array(masses[:-6])*9.81
    plt.plot(forces, distances, "bo", label="measured displacements")
    plt.title("Measured Displacement of Spring")
    plt.xlabel("|Force| (Newtons)")
    plt.ylabel("Distance (meters)")
    #Find linear fit
    a, b = np.polyfit(forces, distances, 1)
    predicted_distances = a*np.array(forces) + b
    k = 1.0 / a
    plt.plot(forces, predicted_distances, label=f"Linear fit, k = {k:.4f}")
    #Cubic fit
    fit = np.polyfit(forces, distances, 3)
    predicted_distances = np.polyval(fit, forces)
    plt.plot(forces, predicted_distances, "k:", label="Cubic fit")
    plt.legend(loc = "best")
    plt.savefig("spring2.jpg")



fit_data("springData.csv")
