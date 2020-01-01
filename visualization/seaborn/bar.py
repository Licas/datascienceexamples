import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv('./visualization/data/survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()