import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('./visualization/data/satisfaction.csv')
print(df)

sns.barplot(
    data=df ,
    x='Gender' ,
    y='Mean Satisfaction'
)

plt.show()