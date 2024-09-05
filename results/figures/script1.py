import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


colors = ['#7DBFAA', '#FF743D', '#5C81D2']


df_ = pd.read_csv("data.csv")
df_ = df_[df_['map1'] != df_['map2']]

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "({:d}) {:.1f}%".format(absolute, pct)




df = df_
# TASKS
nt1 = df[df['task1'].notnull() & df['task2'].isnull()]['uid'].count()
nt2 = df[df['task2'].notnull() & df['task1'].isnull()]['uid'].count()
nt12 = df[(df['task1'].notnull()) & df['task2'].notnull()]['uid'].count()

data = [nt1, nt2, nt12]
plt.figure(figsize=(9,6))
_, _, autotexts = plt.pie(data, labels=['Task 1 only', 'Task 2 only', 'Tasks 1 and 2'], colors=colors, autopct=lambda pct: func(pct, data),
        wedgeprops={'edgecolor':'white'})
for autotext in autotexts:
    autotext.set_color('black')
plt.title("Participation (total: "+str(nt1+nt2+nt12)+")")
plt.show()




df = df_[df_['task2'].notnull()] 
# GENDER
male = df[df['gender']=='Male']['uid'].count()
female = df[df['gender']=='Female']['uid'].count()
na = df[(df['gender']!='Male') & (df['gender']!='Female')]['uid'].count()

data = [male, female, na]
plt.figure(figsize=(9,6))
_, _, autotexts = plt.pie(data, colors=colors, labels=['Male', 'Female', 'No answer'], autopct=lambda pct: func(pct, data),
        wedgeprops={'edgecolor':'white'})
for autotext in autotexts:
    autotext.set_color('black')
plt.title("Gender")
plt.show()



df = df_[df_['task2'].notnull()] 
# AGE
mini = int(df['age'].min())
maxi = int(df['age'].max())
na = df[df['age'].isnull()]['uid'].count()
plt.figure(figsize=(9,6))
_, _, bars = plt.hist(df['age'], color=colors[-1], bins=np.arange(mini, maxi+2)-0.5, zorder=3, rwidth=0.9)
plt.grid(zorder=0, axis='y')
# plt.bar_label(bars)
plt.xticks(range(mini, maxi+1, 3))
plt.ylabel('count')
plt.xlabel('age (years)')
plt.title("Age")
plt.show()



df = df_[df_['task2'].notnull()] 
# POINTING DEVICE
mouse = df[df['pointing']=='Mouse']['uid'].count()
touchpad = df[df['pointing']=='Touchpad']['uid'].count()
touchscreen = df[df['pointing']=='Touchscreen']['uid'].count()
na = df[df['pointing'].isnull()]['uid'].count()

data = [mouse, touchpad, touchscreen]
plt.figure(figsize=(9,6))
_, _, autotexts = plt.pie([mouse, touchpad, touchscreen], colors=colors, labels=['Mouse', 'Touchpad', 'Touchscreen'], autopct=lambda pct: func(pct, data),
        wedgeprops={'edgecolor':'white'})
for autotext in autotexts:
    autotext.set_color('black')
print('na', na)
plt.title("Pointing device")
plt.show()




df = df_[df_['task2'].notnull()] 
# FAMILIARITY GSV
plt.figure(figsize=(9,6))
_, _, bars = plt.hist(df['familiarity'], color=colors[-1], bins=np.arange(1, 7)-0.5, zorder=3, rwidth=0.9)
plt.grid(zorder=0, axis='y')
plt.bar_label(bars)
plt.ylabel('count')
plt.xlabel('familiarity with GSV')
plt.xticks(range(1,6), ['1 (low)', '2', '3', '4', '5 (high)'])
plt.title("Familiarity with GSV interface")
plt.show()



df = df_[df_['task2'].notnull()] 
# FAMILIARITY STUDYAREA
plt.figure(figsize=(9,6))
_, _, bars = plt.hist(df['studyarea'], color=colors[-1], bins=np.arange(1, 7)-0.5, zorder=3, rwidth=0.9)
plt.grid(zorder=0, axis='y')
plt.bar_label(bars)
plt.ylabel('count')
plt.xlabel('familiarity with study area')
plt.xticks(range(1,6), ['1 (low)', '2', '3', '4', '5 (high)'])
plt.title("Familiarity with the study area")
plt.show()



colors = colors[:2]
df = df_
# CONFIDENCE
color = df[df['map1']=='color']['confidence1']
gray = df[df['map1']=='default']['confidence1']

stat, p_value = stats.mannwhitneyu(gray, color, alternative='two-sided')
print("\nConfidence task 1")
print(gray.mean(), color.mean())
print(stat, p_value)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9,6))
fig.suptitle('Confidence level during navigation')

_, _, bars = ax1.hist([gray, color], color=colors, bins=np.arange(1, 7)-0.5, zorder=3, histtype='bar', density=True, label=['gray map', 'color map'])
ax1.grid(zorder=0, axis='y')
ax1.set(xlabel='confidence level', ylabel='relative density')
ax1.set_title("TASK 1")
ax1.set_xticks(range(1,6), ['1 (low)', '2', '3', '4', '5 (high)'])
ax1.set_yticks(np.arange(0, 1, 0.1))
ax1.set_ylim([0, 0.5])
ax1.legend(loc='upper left')
ax1.vlines(gray.mean(), ymin=0, ymax=0.5, zorder=3, color='black')
ax1.vlines(color.mean(), ymin=0, ymax=0.5, zorder=3, color='black', linestyle='dashed')
# ax1.text(gray.mean()+0.05, 0.415, 'mean gray', rotation=90)
# ax1.text(color.mean()-0.25, 0.415, 'mean color', rotation=90)


color = df[df['map2']=='color']['confidence2']
gray = df[df['map2']=='default']['confidence2']

stat, p_value = stats.mannwhitneyu(gray, color, alternative='two-sided')
print("\nConfidence task 2")
print(gray.mean(), color.mean())
print(stat, p_value)

_, _, bars = ax2.hist([gray, color], color=colors, bins=np.arange(1, 7)-0.5, zorder=3, histtype='bar', density=True, label=['gray map', 'color map'])
ax2.grid(zorder=0, axis='y')
ax2.set(xlabel='confidence level', ylabel='relative density')
ax2.set_title("TASK 2")
ax2.set_xticks(range(1,6), ['1 (low)', '2', '3', '4', '5 (high)'])
ax2.set_yticks(np.arange(0, 1, 0.1))
ax2.set_ylim([0,0.5])
ax2.legend()
ax2.vlines(gray.mean(), ymin=0, ymax=0.5, zorder=3, color='black')
ax2.vlines(color.mean(), ymin=0, ymax=0.5, zorder=3, color='black', linestyle='dashed')
ax2.text(gray.mean()-0.25, 0.415, 'mean gray', rotation=90)
ax2.text(color.mean()-0.25, 0.415, 'mean color', rotation=90)

plt.show()









df = df_
# INFORMATION
color = df[df['map1']=='color']['information1']
gray = df[df['map1']=='default']['information1']

stat, p_value = stats.mannwhitneyu(gray, color, alternative='two-sided')
print("\nInformation task 1")
print(gray.mean(), color.mean())
print(stat, p_value)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9,6))
fig.suptitle('Amount of information on the map')

_, _, bars = ax1.hist([gray, color], color=colors, bins=np.arange(1, 7)-0.5, zorder=3, histtype='bar', density=True, label=['gray map', 'color map'])
ax1.grid(zorder=0, axis='y')
ax1.set(xlabel='information level', ylabel='relative density')
ax1.set_title("TASK 1")
ax1.set_xticks(range(1,6), ['1 (low)', '2', '3 (ideal)', '4', '5 (high)'])
ax1.set_yticks(np.arange(0, 1, 0.1))
ax1.set_ylim([0,0.55])
ax1.legend()
ax1.vlines(gray.mean(), ymin=0, ymax=1, zorder=3, color='black')
ax1.vlines(color.mean(), ymin=0, ymax=1, zorder=3, color='black', linestyle='dashed')
# ax1.text(gray.mean()-0.25, 0.45, 'mean gray', rotation=90)
# ax1.text(color.mean()+0.05, 0.45, 'mean color', rotation=90)


color = df[df['map2']=='color']['information2']
gray = df[df['map2']=='default']['information2']

stat, p_value = stats.mannwhitneyu(gray, color, alternative='two-sided')
print("\nInformation task 2")
print(gray.mean(), color.mean())
print(stat, p_value)

_, _, bars = ax2.hist([gray, color], color=colors, bins=np.arange(1, 7)-0.5, zorder=3, histtype='bar', density=True, label=['gray map', 'color map'])
ax2.grid(zorder=0, axis='y')
ax2.set(xlabel='information level', ylabel='relative density')
ax2.set_title("TASK 2")
ax2.set_xticks(range(1,6), ['1 (low)', '2', '3 (ideal)', '4', '5 (high)'])
ax2.set_yticks(np.arange(0, 1, 0.1))
ax2.set_ylim([0,0.55])
ax2.legend()
ax2.vlines(gray.mean(), ymin=0, ymax=1, zorder=3, color='black')
ax2.vlines(color.mean(), ymin=0, ymax=1, zorder=3, color='black', linestyle='dashed')
ax2.text(gray.mean()-0.25, 0.45, 'mean gray', rotation=90)
ax2.text(color.mean()+0.05, 0.38, 'mean color', rotation=90)

plt.show()




df = df_
# RATIO
color1 = df[df['map1']=='color']['ratio1']
gray1 = df[df['map1']=='default']['ratio1']

t_statistic, p_value = stats.ttest_ind(gray1, color1)
print("\nInside-outside ratio task 1")
print(gray1.mean(), color1.mean())
print(t_statistic, p_value)

color2 = df[df['map2']=='color']['ratio2']
gray2 = df[df['map2']=='default']['ratio2']

t_statistic, p_value = stats.ttest_ind(gray2, color2)
print("\nInside-outside ratio task 2")
print(gray2.mean(), color2.mean())
print(t_statistic, p_value)

plt.figure(figsize=(9,6))
bp = plt.boxplot([gray1, color1, [], gray2, color2], showmeans=True, meanline=True, zorder=3, patch_artist=True, widths=.8)
plt.grid(zorder=0, axis='y')
plt.ylabel('inside-outside ratio')
plt.xticks([1.5,4.5], ['TASK 1', 'TASK 2'])
plt.title("Navigation on the route")

for patch, color in zip(bp['boxes'], colors + ['#FFFFFF'] + colors):
    patch.set(facecolor = color,
              color=color)

for flier in bp['fliers']:
    flier.set(marker ='+',
              alpha = 0.5)

for median in bp['medians']:
    median.set(linewidth = 1,
              linestyle='-',
              color='black')
    
for mean in bp['means']:
    mean.set(linewidth = 1,
              linestyle='dashed',
              color='black')
    
custom_legend = [Patch(facecolor=colors[0], label='gray map'), 
                 Patch(facecolor=colors[1], label='color map'),
                 Line2D([0], [0], color='black', linestyle='dashed', label='mean'),
                 Line2D([0], [0], color='black', linestyle='-', label='median')] 
plt.legend(handles=custom_legend)
    
plt.show()




df = df_
# EXPLORATION
color1 = df[df['map1']=='color']['explore1']
gray1 = df[df['map1']=='default']['explore1']

t_statistic, p_value = stats.ttest_ind(gray1, color1)
print("\nExploration score task 1")
print(gray1.mean(), color1.mean())
print(t_statistic, p_value)

color2 = df[df['map2']=='color']['explore2']
gray2 = df[df['map2']=='default']['explore2']

t_statistic, p_value = stats.ttest_ind(gray2, color2)
print("\nExploration score task 2")
print(gray2.mean(), color2.mean())
print(t_statistic, p_value)

plt.figure(figsize=(9,6))
bp = plt.boxplot([gray1, color1, [], gray2, color2], showmeans=True, meanline=True, zorder=3, patch_artist=True, widths=.8)
plt.grid(zorder=0, axis='y')
plt.ylabel('exploration score')
plt.xticks([1.5,4.5], ['TASK 1', 'TASK 2'])
plt.title("Exploration during navigation")

for patch, color in zip(bp['boxes'], colors + ['#FFFFFF'] + colors):
    patch.set(facecolor = color,
              color=color)

for flier in bp['fliers']:
    flier.set(marker ='+',
              alpha = 0.5)

for median in bp['medians']:
    median.set(linewidth = 1,
              linestyle='-',
              color='black')
    
for mean in bp['means']:
    mean.set(linewidth = 1,
              linestyle='dashed',
              color='black')
    
custom_legend = [Patch(facecolor=colors[0], label='gray map'), 
                 Patch(facecolor=colors[1], label='color map'),
                 Line2D([0], [0], color='black', linestyle='dashed', label='mean'),
                 Line2D([0], [0], color='black', linestyle='-', label='median')] 
plt.legend(handles=custom_legend)
    
plt.show()






df = df_
# ARRIVAL
color1 = df[df['map1']=='color']['arrival1']
gray1 = df[df['map1']=='default']['arrival1']

color2 = df[df['map2']=='color']['arrival2']
gray2 = df[df['map2']=='default']['arrival2']

color = [color1.sum(), color2.sum()]
gray = [gray1.sum(), gray2.sum()]

ncolor = [color1.count() - color1.sum(), color2.count() - color2.sum()]
ngray = [gray1.count() - gray1.sum(), gray2.count() - gray2.sum()]


data = np.array([[color[0], ncolor[0]], [gray[0], ngray[0]]])
chi2_stat, p_value, dof, expected = stats.chi2_contingency(data)
print("\nArrival task 1")
print(gray[0], ngray[0], color[0], ncolor[0])
print(chi2_stat, p_value)

data = np.array([[color[1], ncolor[1]], [gray[1], ngray[1]]])
chi2_stat, p_value, dof, expected = stats.chi2_contingency(data)
print("\nArrival task 2")
print(gray[1], ngray[1], color[1], ncolor[1])
print(chi2_stat, p_value)


plt.figure(figsize=(9,6))
bars = plt.bar([0,0.75], gray, width=0.25, zorder=3, color=colors[0], label='gray map')
rectsG = bars.patches
for rect, val in zip(rectsG, gray):
    height = rect.get_height()/2 -1
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(val) + "\nsuccess", ha="center", va="bottom")

bars = plt.bar([0.25,1], color, width=0.25, zorder=3, color=colors[1], label='color map')
rectsC = bars.patches
for rect, val in zip(rectsC, color):
    height = rect.get_height()/2 -1
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(val) + "\nsuccess", ha="center", va="bottom")

bars = plt.bar([0,0.75], ngray, width=0.25, zorder=3, bottom=gray, color=colors[0], alpha=.4)
rects = bars.patches
for rect, rectG, val in zip(rects, rectsG, ngray):
    height = rect.get_height()/2 + rectG.get_height()-1
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(val) + " fail", ha="center", va="bottom")

bars = plt.bar([0.25,1], ncolor, width=0.25, zorder=3, bottom=color, color=colors[1], alpha=.4)
rects = bars.patches
for rect, rectC, val in zip(rects, rectsC, ncolor):
    height = rect.get_height()/2 + rectC.get_height()-1
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(val) + " fail", ha="center", va="bottom")

plt.grid(zorder=0, axis='y')
plt.ylabel('count')
plt.xticks([0.125,0.875], ['TASK 1', 'TASK 2'])
plt.title("Arrival on the final location")
plt.legend()



plt.show()





