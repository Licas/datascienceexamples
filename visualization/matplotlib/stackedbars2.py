from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

#create your plot here
fig = plt.figure(figsize=(10,8))
ax = plt.subplot()

plt.bar(x, As, label='A')
plt.bar(x, Bs, label='B', bottom=As)
plt.bar(x, Cs, label='C', bottom=c_bottom)
plt.bar(x, Ds, label='D', bottom=d_bottom)
plt.bar(x, Fs, label='F', bottom=f_bottom)

plt.legend(loc=3)

ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

plt.show()

plt.savefig('my_stacked_bar.png')