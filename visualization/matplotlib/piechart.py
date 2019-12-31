from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

# Pie Chart with payment methods distribution
# autopct used to show percentage on pie slices
plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')

# Needed to make a circle
plt.axis('equal')

plt.legend(payment_method_names)

plt.show()