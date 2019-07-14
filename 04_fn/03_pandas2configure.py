import pandas
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set()
axi_2 = []
for i in range(40):
    temp = []
    for j in range(40):
        temp.append(random.randint(-100, 100))
    axi_2.append(temp)


pd = pandas.DataFrame(axi_2)


fig, ax = plt.subplots(figsize=(40, 40))

sns.heatmap(pd, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()
