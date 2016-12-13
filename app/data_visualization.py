#!/usr/bin/env python
from matplotlib import pyplot
from pandas.tools.plotting import scatter_matrix
import load_dataset as load

dataset = load.dataset()

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# histograms
dataset.hist()
# scatter plot matrix
scatter_matrix(dataset)


if __name__ == '__main__':
    # Open UI with graphs
    pyplot.show()
