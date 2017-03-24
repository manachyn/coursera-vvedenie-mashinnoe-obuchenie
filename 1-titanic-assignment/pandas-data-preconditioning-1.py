from __future__ import print_function
import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

sex_counts = data['Sex'].value_counts()
male_count = sex_counts['male']
female_count = sex_counts['female']

print('Male:   ', male_count)
print('Female: ', female_count)

file = open('result-1.txt', 'w')
print(male_count, ' ', female_count, file=file, sep='', end='')
file.close()
