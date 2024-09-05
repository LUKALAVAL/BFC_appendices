from skimage import color
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math
from matplotlib.lines import Line2D



# Parameters
filenames = [
's0.csv',
's1.csv',
's2.csv',
's3.csv',
's4.csv',
's5.csv',
's6.csv'
]



# Convert HEX color to CIELAB
def hex_to_lab(hex):
    rgb = np.array(tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))
    lab = color.rgb2lab(rgb / 255.0)
    return lab

# Convert CIELAB color to HEX
def lab_to_hex(lab):
    rgb = color.lab2rgb(lab) * 255
    hex = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2])).upper()
    return hex



# Delta E76 (distance calculation)
def ciede76(lab1, lab2):
    return np.linalg.norm(lab1-lab2)

# Delta E00 (distance calculation)
def ciede00(lab1, lab2):
    L1,a1,b1 = lab1
    L2,a2,b2 = lab2
    # CIEDE2000 color difference formula implementation
    L_bar_prime = 0.5 * (L1 + L2)
    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    C_bar = 0.5 * (C1 + C2)
    G = 0.5 * (1 - math.sqrt((C_bar**7) / (C_bar**7 + 25**7)))
    a1_prime = (1 + G) * a1
    a2_prime = (1 + G) * a2
    C1_prime = math.sqrt(a1_prime**2 + b1**2)
    C2_prime = math.sqrt(a2_prime**2 + b2**2)
    C_bar_prime = 0.5 * (C1_prime + C2_prime)
    h1_prime = math.degrees(math.atan2(b1, a1_prime)) % 360
    h2_prime = math.degrees(math.atan2(b2, a2_prime)) % 360
    H_bar_prime = 0.5 * (h1_prime + h2_prime)

    if abs(h1_prime - h2_prime) > 180:
        H_bar_prime += 180

    T = 1 - 0.17 * math.cos(math.radians(H_bar_prime - 30)) + \
        0.24 * math.cos(math.radians(2 * H_bar_prime)) + \
        0.32 * math.cos(math.radians(3 * H_bar_prime + 6)) - \
        0.20 * math.cos(math.radians(4 * H_bar_prime - 63))

    delta_h_prime = h2_prime - h1_prime

    if abs(delta_h_prime) > 180:
        if h2_prime <= h1_prime:
            delta_h_prime += 360
        else:
            delta_h_prime -= 360

    delta_L_prime = L2 - L1
    delta_C_prime = C2_prime - C1_prime
    delta_H_prime = 2 * math.sqrt(C1_prime * C2_prime) * math.sin(math.radians(0.5 * delta_h_prime))

    S_L = 1 + ((0.015 * ((L_bar_prime - 50)**2)) / math.sqrt(20 + ((L_bar_prime - 50)**2)))
    S_C = 1 + 0.045 * C_bar_prime
    S_H = 1 + 0.015 * C_bar_prime * T

    delta_theta = 30 * math.exp(-((H_bar_prime - 275) / 25)**2)
    R_C = 2 * math.sqrt((C_bar_prime**7) / (C_bar_prime**7 + 25**7))
    R_T = -R_C * math.sin(math.radians(2 * delta_theta))

    delta_E = math.sqrt(
        (delta_L_prime / S_L)**2 +
        (delta_C_prime / S_C)**2 +
        (delta_H_prime / S_H)**2 +
        R_T * (delta_C_prime / S_C) * (delta_H_prime / S_H)
    )

    return delta_E



# Read colors from files and store them into HEX list and LAB list
hex_mat = []
lab_mat = []
for filename in filenames:
    file = open(filename, 'r')
    hex = [line[:7] for line in file]
    lab = [hex_to_lab(c) for c in hex]
    hex_mat.append(hex)
    lab_mat.append(lab)

hex_mat = np.array(hex_mat)
lab_mat = np.array(lab_mat)



# Calculate the distances between colors
dist_mat = []
lab1 = lab_mat[0]
for lab2 in lab_mat:
    dist = []
    for c1,c2 in zip(lab1, lab2):
        dist.append(ciede00(c1,c2))
    dist_mat.append(dist)

dist_mat = np.array(dist_mat)


# Display the distances

plt.figure(figsize=(10,6))



for i in range(1, len(dist_mat)):
    dist = dist_mat[i]
    plt.plot(dist, '-', color='grey', linewidth=1, markersize=12, label='sn')
    for j in range(len(dist)):
        plt.plot(j, dist[j], color=hex_mat[i,j], marker='o', markersize=10)

dist = dist_mat[0]
plt.plot(dist, '-s', color='black', linewidth=1, markersize=12, label='s0')
for j in range(len(dist)):
    plt.plot(j, dist[j], color=hex_mat[0,j], marker='s', markersize=10)

plt.plot(np.mean(dist_mat[1:], axis=0), '+', color='black', markersize=15)

plt.xticks(list(range(len(dist_mat[0]))), ['b'+str(i) for i in range(len(dist_mat[0]))])
plt.hlines(y=[10], xmin=-1, xmax=len(dist), linestyles='--', color='grey', linewidth=0.9)

plt.xlim([-1,len(dist_mat[0])])
plt.legend(handles=[Line2D([0], [0], ls='-', color='grey', ms=12, marker='o', label='s1..6'),
                    Line2D([0], [0], ls='-', color='black', ms=12, marker='s', label='s0'),
                    Line2D([0], [0], ls='', color='black', ms=15, marker='+', label='mean')])
plt.xlabel('Building')
plt.ylabel('Delta E')
# plt.title('Distances to s0')
plt.show()







# Creating plot
plt.figure(figsize=(10,6))

for i in range(1, len(dist_mat)):
    for j in range(len(dist)):
        plt.plot(j+1, dist_mat[i,j], color=hex_mat[i,j], marker='o', markersize=10)

bp = plt.boxplot(dist_mat[1:], showmeans=True, meanline=True)

# for mean in bp['means']:
#     mean.set_color('blue')

for mean in bp['means']:
    mean.set_color('red')


plt.hlines(y=[10,49], xmin=1, xmax=len(dist), linestyles='dotted', color='black', linewidth=0.9)
plt.xlabel('Building')
plt.ylabel('Delta E')
plt.title('Boxplots of distances to s0')
meanLine = mlines.Line2D([], [], color='blue', label='mean', linestyle='dashed')
medLine = mlines.Line2D([], [], color='orange', label='median')
plt.legend(handles=[meanLine, medLine])
