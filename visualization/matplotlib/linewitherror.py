from matplotlib import pyplot as plt

#Future revenue projection
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]


# fill_between parameters
# plt.fill_between(x_values, y_lower, y_upper, alpha=0.2)

# lower bounds
y_lower = [i - 0.1 * i for i in revenue]
# upper bounds
y_upper = [i + 0.1 * i for i in revenue]

# Plot the bounds with alpha 0.2
plt.fill_between(months, y_lower,y_upper,alpha=0.2)

# Plot the actual revenues
plt.plot(months, revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)


plt.show()