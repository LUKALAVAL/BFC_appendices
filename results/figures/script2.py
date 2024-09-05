import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


colors = ['#7DBFAA', '#FF743D', '#5C81D2']

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "({:d}) {:.1f}%".format(absolute, pct)


df_ = pd.read_csv("data.csv")
df_ = df_[df_['map1'] != df_['map2']]

df = df_

print(df[df['information1'] > df['information2']]['map1'].describe(), '\n')
print(df[df['information1'] < df['information2']]['map2'].describe(), '\n')
print(df[df['information1'] == df['information2']]['uid'].describe(), '\n')

data = [6, 32, 36]
plt.figure(figsize=(9,6))
plt.pie(data, labels=['Gray map', 'Color map', 'No preference'], colors=colors, autopct=lambda pct: func(pct, data),
        wedgeprops={'edgecolor':'white'})
plt.title('Relative rating (amount of information)')
plt.show()





print(df[df['confidence1'] > df['confidence2']]['map1'].describe(), '\n')
print(df[df['confidence1'] < df['confidence2']]['map2'].describe(), '\n')
print(df[df['confidence1'] == df['confidence2']]['uid'].describe(), '\n')

data = [11, 26, 37]
plt.figure(figsize=(9,6))
plt.pie(data, labels=['Gray map', 'Color map', 'No preference'], colors=colors, autopct=lambda pct: func(pct, data),
        wedgeprops={'edgecolor':'white'})
plt.title('Relative rating (confidence)')
plt.show()



