from __future__ import print_function
import pandas
from sklearn.tree import DecisionTreeClassifier

df = pandas.read_csv('titanic.csv', index_col='PassengerId')

df2 = df[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']].dropna()
df2['Sex'] = df2['Sex'].map(lambda x: 1 if x == 'male' else -1)

features = ['Pclass', 'Fare', 'Age', 'Sex']
target = 'Survived'

X = df2[features]
y = df2[target]

classifier = DecisionTreeClassifier(random_state=241)
classifier.fit(X, y)

importances = pandas.Series(classifier.feature_importances_, index=features)

file = open('result.txt', 'w')
print(' '.join(importances.sort_values(ascending=False).head(2).index.values), file=file, sep='', end='')
file.close()
