import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from shad_util import print_answer
import sys
sys.path.append("..")


outFile1 = open('01Zadanie.txt', 'w', encoding='utf8')

# 1. Загрузите выборку из файла titanic.csv с помощью пакета Pandas.

df = pd.read_csv('titanic.csv', index_col='PassengerId')

# 2. Оставьте в выборке четыре признака: класс пассажира (Pclass), цену билета (Fare),
# возраст пассажира (Age) и его пол (Sex).

x_labels = ['Pclass', 'Fare', 'Age', 'Sex']
X = df.loc[:, x_labels]

# 3. Обратите внимание, что признак Sex имеет строковые значения.

X['Sex'] = X['Sex'].map(lambda sex: 1 if sex == 'male' else 0)

# 4. Выделите целевую переменную — она записана в столбце Survived.

y = df['Survived']

# 5. В данных есть пропущенные значения — например, для некоторых пассажиров неизвестен их возраст.
# Такие записи при чтении их в pandas принимают значение nan. Найдите все объекты, у которых есть пропущенные признаки,
# и удалите их из выборки.

X = X.dropna()
y = y[X.index.values]

# 6. Обучите решающее дерево с параметром random_state=241 и остальными параметрами по умолчанию.

clf = DecisionTreeClassifier(random_state=241)
clf.fit(np.array(X.values), np.array(y.values))

# 7. Вычислите важности признаков и найдите два признака с наибольшей важностью.
# Их названия будут ответами для данной задачи (в качестве ответа укажите названия признаков через запятую или пробел,
# порядок не важен).

importances = pd.Series(clf.feature_importances_, index=x_labels)
print(' '.join(importances.sort_values(ascending=False).head(2).index.values), file=outFile1)
#print_answer(1, ' '.join(importances.sort_values(ascending=False).head(2).index.values))

outFile1.close()
