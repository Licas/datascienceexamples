from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
plt.close('all')

# Viewers by game
ax = plt.subplot()
plt.bar(range(len(games)), viewers, color='cadetblue', label="Games")
plt.title("Viewers count by Game")

ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation=30)
ax.set_xlabel('Game')
ax.set_ylabel('#Viewers')

plt.legend(loc=1)

plt.show()
plt.clf()

ax2 = plt.subplot()
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(x=countries, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%1.0f%%', pctdistance=0.85, startangle=345)

ax2.axis('equal')
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")

plt.show()
plt.clf()

yupper = [i+i*0.15 for i in viewers_hour]
ylower = [i-i*0.15 for i in viewers_hour]

ax3 = plt.subplot()
ax3.set_xticks(hour)

plt.fill_between(hour, ylower,yupper, alpha=0.2)
plt.plot(hour, viewers_hour)
plt.title("Viewers by hour")

plt.show()

