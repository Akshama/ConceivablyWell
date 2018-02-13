# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 05:21:37 2018

@author: Akshama PC
"""

# Univariate Histograms
import matplotlib.pyplot as plt
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'glucose', 'pres', 'skin', 'insulin', 'bmi', 'pedi', 'age', 'outcome-0 or 1']
data = pandas.read_csv(url, names=names)
data.hist()
plt.show()

# Correction Matrix Plot
import matplotlib.pyplot as plt
import pandas
import numpy
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()
