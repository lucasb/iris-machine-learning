#!/usr/bin/env python

from matplotlib import pyplot
import select_model

# get rank of models and build list for results and names
rank = select_model.ranking()
results = list(map(lambda i: i[3], rank))
names = list(map(lambda i: i[0], rank))

# set info to graph as name
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)

# set lists to graph
pyplot.boxplot(results)
ax.set_xticklabels(names)


if __name__ == '__main__':
    # open ui with graph
    pyplot.show()
