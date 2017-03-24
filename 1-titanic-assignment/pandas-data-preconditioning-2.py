from __future__ import print_function
import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

survived = data['Survived']
survived_counts = survived.value_counts()
survived_percent = 100.0 * survived_counts[1] / survived.size

print(survived_percent)

file = open('result-2.txt', 'w')
print('{0:.2f}'.format(survived_percent), file=file, sep='', end='')
file.close()
