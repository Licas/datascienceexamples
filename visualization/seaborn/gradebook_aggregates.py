import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

gradebook = pd.read_csv("./visualization/data/gradebook.csv")

#print(gradebook)
assignment1 = gradebook[gradebook['assignment_name']=='Assignment 1']

#print(assignment1)

asn1_median = np.median(assignment1['grade'])
print("Median of Assignmen1 grades:",asn1_median)


assign_mean = gradebook.groupby('assignment_name').grade.mean().reset_index()

#print(assign_mean)
''' sns.barplot( x='assignment_name',y='grade', 
    data=assign_mean, 
    ci='sd')
'''
sns.barplot( x='assignment_name',y='grade', 
    data=gradebook, 
    ci='sd',
 estimator=np.median)

plt.show()