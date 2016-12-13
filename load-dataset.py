#!/usr/bin/env python

import pandas


file_path = 'iris.data'
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(file_path, names=col_names)


if __name__ == '__main__':
    # shape (total rows, total cols)
    print(dataset.shape)
    # head (top N=5 rows)
    print(dataset.head(5))
    # descriptions (statistical summary)
    print(dataset.describe())
    # distribution by class
    print(dataset.groupby(by='class').size())
