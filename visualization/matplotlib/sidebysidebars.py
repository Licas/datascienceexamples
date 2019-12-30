from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
sales3 = [165, 18, 32, 50, 88, 70]


def compute_bar_xvalues(datasetIndex,totalDatasets, numberOfBarsForDataset, barWidth):
    return [totalDatasets * element + barWidth * datasetIndex for element in range(numberOfBarsForDataset)]

n = 1  # This is our first dataset (out of 2)
t = 3 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = compute_bar_xvalues(n,t,d,w)

n = 2
store2_x = compute_bar_xvalues(n,t,d,w)

n = 3
store3_x = compute_bar_xvalues(n,t,d,w)

plt.bar( store1_x, sales1)
plt.bar( store2_x, sales2)
plt.bar( store3_x, sales3)

plt.legend(['Sales 1','Sales 2','Sales 3'])
plt.show()
