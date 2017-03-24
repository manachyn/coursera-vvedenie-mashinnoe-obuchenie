from __future__ import print_function

import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

ages = data['Age'].dropna()

ages_mean = ages.mean()
ages_median = ages.median()

print('Ages mean:', ages_mean)
print('Ages median:', ages_median)

file = open('result-4.txt', 'w')
print('{0:.2f}'.format(ages_mean), ' ', '{0:.2f}'.format(ages_median), file=file, sep='', end='')
file.close()
