from __future__ import print_function
import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

pclass = data['Pclass']
pclass_counts = pclass.value_counts()
pclass_percent = 100.0 * pclass_counts[1] / pclass.size

print(pclass_percent)

file = open('result-3.txt', 'w')
print('{0:.2f}'.format(pclass_percent), file=file, sep='', end='')
file.close()
