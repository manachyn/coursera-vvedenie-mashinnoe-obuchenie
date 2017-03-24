from __future__ import print_function

import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

correlation = data['SibSp'].corr(data['Parch'])

print('Correlation:', correlation)

file = open('result-5.txt', 'w')
print('{0:.2f}'.format(correlation), file=file, sep='', end='')
file.close()
