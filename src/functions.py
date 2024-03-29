from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def get_static_file(file_name):
    return Path("static/" + file_name)


def count_labels(index, arr):
    labels = {}
    for item in arr:
        key = item[index]
        if key in labels:
            labels[key] += 1
        elif key not in labels:
            labels[key] = 0
    return labels


def print_graph(labels_dict, y_label, save_name='default.pdf'):
    x_axis = list(labels_dict.keys())
    y_axis = list(labels_dict.values())
    plt.xlabel('Occurences')
    plt.ylabel(y_label)
    plt.title('Number of Occurences for each ' + y_label + ' Found in the Dictionary GoEmotion')
    plt.barh(x_axis, y_axis)  # printed vertically to better show the labels
    plt.savefig(get_static_file(save_name), bbox_inches="tight")
    plt.show()


def convert_label_to_index(arr, labels):
    converted_arr = np.zeros(arr.size)
    for i, element in enumerate(arr):
        converted_arr[i] = np.where(labels == element)[0][0]
    return converted_arr

def performance_output(f, model, classification, hyperparameter, confusion_matrix, evaluation_metrics):
    f.write("Model: %s\nClassification: %s\nHyperparameter: %s\nConfusion matrix:\n %s\nEvaluation Metrics:\n%s" %(model, classification, hyperparameter, confusion_matrix, evaluation_metrics));