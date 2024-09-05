# Before running the script, make sure the building layer is not in edit mode on QGIS

import colorsys
from skimage import color
from sklearn.cluster import MeanShift
import numpy as np
from qgis.core import QgsProject, QgsVectorLayer, QgsField, edit
from PyQt5.QtCore import QVariant




layer_name = 'building'
color_field = 'color'
bandwidth_list = [1,2,3,4,5,6,7,8,9,10,11,13,16,20,50]
new_color_field = 'color_ms' # This is the first part of the new color field's name





def hex_to_lab(hex):
    rgb = tuple(int(hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    lab = color.rgb2lab(np.array(rgb) / 255.0)
    return lab

def lab_to_hex(lab):
    rgb = color.lab2rgb(lab)
    hex = '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)).upper()
    return hex





layer = QgsProject.instance().mapLayersByName(layer_name)[0]

for bandwidth in bandwidth_list:
    colors_hex = []
    colors_lab = []
    colors_hex_valid = []
    colors_lab_valid = []
    for feature in layer.getFeatures():
        hex = feature[color_field]
        if hex is None or not isinstance(hex, str) or len(hex) != 7 or not hex.startswith('#'):
            colors_hex.append(None)
            colors_lab.append(None)
        else:
            lab = hex_to_lab(hex)
            colors_hex.append(hex)
            colors_lab.append(lab)
            colors_hex_valid.append(hex)
            colors_lab_valid.append(lab)
    



    meanshift = MeanShift(bandwidth=bandwidth).fit(colors_lab_valid)
    labels = meanshift.labels_


    cluster_means_hex = []
    for cluster_label in range(max(labels)+1):
        elements_id = np.where(labels == cluster_label)[0]
        elements_color = [colors_lab_valid[id] for id in elements_id]
        cluster_mean_lab = tuple(np.mean(elements_color, axis=0))
        cluster_mean_hex = lab_to_hex(cluster_mean_lab)
        cluster_means_hex.append(cluster_mean_hex)

    new_color_field_fullname = new_color_field + str(bandwidth)
    if layer.fields().indexOf(new_color_field_fullname) == -1:
        layer.dataProvider().addAttributes([QgsField(new_color_field_fullname, QVariant.String)])
        layer.updateFields()

    with edit(layer):
        for feature in layer.getFeatures():
            hex_color = feature[color_field]
            if hex_color in colors_hex_valid:
                label = labels[colors_hex_valid.index(hex_color)]
                feature[new_color_field_fullname] = cluster_means_hex[label]
                layer.updateFeature(feature)

    unique, counts = np.unique(labels, return_counts=True)
        
    print(np.size(counts), bandwidth, np.sort(counts))


print("Done; bandwidths:", bandwidth_list)

