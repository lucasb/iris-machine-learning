#!/usr/bin/env python

import os
import pandas

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path + '/../resources/iris.data'
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']


def dataset():
    return pandas.read_csv(file_path, names=col_names)

if __name__ == '__main__':
    dataset = dataset()
    # shape (total rows, total cols)
    print(dataset.shape)
    # head (top N=5 rows)
    print(dataset.head(5))
    # descriptions (statistical summary)
    print(dataset.describe())
    # distribution by class
    print(dataset.groupby(by='class').size())
