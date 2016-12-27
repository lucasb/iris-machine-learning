#!/usr/bin/env python

from matplotlib import pyplot
import select_model


rank = select_model.ranking()
results = list(map(lambda i: i[3], rank))
names = list(map(lambda i: i[0], rank))

fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')

ax = fig.add_subplot(111)

pyplot.boxplot(results)
ax.set_xticklabels(names)


if __name__ == '__main__':
    pyplot.show()
