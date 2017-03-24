from __future__ import print_function

import pandas, re

def extract_first_name(name):
    match = re.match('([^,]+), ([^.]+)\. ([^()]+)?(\(([^")]+)\))? ?(\("([^)]+)"\))?', name)

    full_name = None

    if match:
        if match.group(5):
            full_name = match.group(5)
        else:
            full_name = match.group(3)

    first_name = full_name.split()[0]

    return first_name


data = pandas.read_csv('titanic.csv', index_col='PassengerId')

names = data[data['Sex'] == 'female']['Name'].map(extract_first_name)
names_counts = names.value_counts()
most_popular_name = names_counts.head(1).keys()[0]

print('Most popular female name:', most_popular_name)

file = open('result-6.txt', 'w')
print(most_popular_name, file=file, sep='', end='')
file.close()
