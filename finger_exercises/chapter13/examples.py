import matplotlib.pyplot as plt


principal = 10000
rate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * rate
plt.plot(values, "b-")
plt.title("5 % Growth, compounding annualy", fontsize= "xx-large")
plt.xlabel("Years of Compounding", fontsize="x-small")
plt.ylabel("Value of Principal in USD")