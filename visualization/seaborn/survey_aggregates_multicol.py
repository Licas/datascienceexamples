import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

survey = pd.read_csv("./visualization/data/survey.csv")

#print(gradebook)

sns.barplot( x='Gender',y='Response', 
    data=survey, 
    ci='sd',
    hue='Age Range')

plt.show()