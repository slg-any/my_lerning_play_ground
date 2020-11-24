"""
import numpy as np
import matplotlib.pyplot as plt

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35
fig, ax = plt.subplots()
ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,label='Women')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()

"""
import sys
sys.path.append("C:\\Users\\NaiduSwathi\\AppData\\Roaming\\Python\\Python37\\site-packages\\matplotlib")
print(sys.path)

import matplotlib.pyplot

print("after matplotlib import")

dev_x = [23, 25, 27, 29, 31]
dev_y = [25000, 28000, 30000, 32000, 35000]

matplotlib.pyplot.plot(dev_x, dev_y)
matplotlib.pyplot.show()
