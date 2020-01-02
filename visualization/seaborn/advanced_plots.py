import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("./visualization/data/advanced/dataset1.csv", delimiter=",")
set_two = np.genfromtxt("./visualization/data/advanced/dataset2.csv", delimiter=",")
set_three = np.genfromtxt("./visualization/data/advanced/dataset3.csv", delimiter=",")
set_four = np.genfromtxt("./visualization/data/advanced/dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500 #n is the number of elements in the datasets
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

fig = plt.figure()
# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

#Creating a barplot
fig.add_subplot(4,1,1)
sns.barplot(data=df,  x="label", y="value")


fig.add_subplot(4,1,2)

sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)

plt.legend(['Set One','Set Two','Set Three','Set Four'])


fig.add_subplot(4,2,7)
sns.boxplot(data=df, x='label',y='value')

#Violin plot
fig.add_subplot(4,2,8)
sns.violinplot(data=df, x='label',y='value')

plt.show()

