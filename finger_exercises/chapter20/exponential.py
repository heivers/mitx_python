import numpy as np
import matplotlib.pyplot as plt
import os
import sys

os.chdir(sys.path[0])

vals = []
for i in range(10):
    vals.append(3**i)
plt.plot(vals, "ko", label = "Actual points")
xVals = np.arange(10)
fit = np.polyfit(xVals, vals, 5)
y_vals = np.polyval(fit, xVals)
plt.plot(y_vals, "kx", label="Predicted Points", markeredgewidth=2, markersize=25)
plt.title("fitting y = 3**x")
plt.legend(loc="upper left")
plt.savefig("Exponential.jpg")
plt.clf()

#plotting the log of an exponential function
x_vals = [x for x in range(10)]
y_vals = [3**y for y in range(10)]
plt.plot(x_vals, y_vals)
plt.savefig("exponential_func.jpg")
plt.clf()
plt.plot(x_vals, y_vals)
plt.semilogy()
plt.savefig("semilog_exponential.jpg")


print(f"Model predicts that 3**20 is roughly {np.polyval(fit, [3**20])[0]}")
print(f"3**20 is actually {3**20}")