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
sns.set_style("whitegrid")
#Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.
sns.set_palette("deep")
'''
In addition to the default palette and its variations, 
Seaborn also allows the use of Color Brewer palettes. 
Color Brewer is the name of a set of color palettes inspired by 
the research of cartographer Cindy Brewer. 
The color palettes are specifically chosen to be easy to interpret
when used to represent ordered categories. 
They are also colorblind accessible, as each color differs from its neighbors 
in lightness or tint.
To use, pass the name of any Color Brewer palette directly to any of the color functions:
    custom_palette = sns.color_palette("Paired", 9)
    sns.palplot(custom_palette)
'''
#sns.despine()

#Creating a barplot
fig.add_subplot(2,1,1)
sns.set_context("poster")
sns.barplot(data=df,  x="label", y="value")


fig.add_subplot(2,1,2)
sns.set_context("paper")
sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)

plt.legend(['Set One','Set Two','Set Three','Set Four'])
# plt.show()

#Box Plot
fig2=plt.figure(2)
fig2.add_subplot(2,1,1)
sns.set_context("notebook")
sns.boxplot(data=df, x='label',y='value')

#Violin plot
# fig2.add_subplot(4,2,8)
fig2.add_subplot(2,1,2)
#rc stands for run command and overrides a specific value from seaborn dictionary -> sns.plotting_context()
sns.set_context("talk",font_scale = .5, rc={"grid.linewidth": 0.6})
sns.violinplot(data=df, x='label',y='value')

# Color Palette
#palette = sns.color_palette("bright")
#sns.palplot(palette)

#sns.despine()
plt.show()

