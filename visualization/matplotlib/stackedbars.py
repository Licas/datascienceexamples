from matplotlib import pyplot as plt
import numpy as np

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
sales3 = [165, 18, 32, 50, 88, 70]

plt.title("Sales by drink type")
plt.xlabel("Drink type")
plt.ylabel("# of sales")
plt.bar(range(len(drinks)),sales1,label="Atlanta")
plt.bar(range(len(drinks)),sales2,bottom=sales1, label="San Francisco")
plt.bar(range(len(drinks)),sales3,bottom=np.array(sales1)+np.array(sales2), label="New york")

plt.legend(loc=1)
plt.show()