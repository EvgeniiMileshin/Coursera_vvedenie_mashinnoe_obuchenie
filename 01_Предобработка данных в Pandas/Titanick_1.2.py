import pandas as pd
import re

outFile1 = open('01Zadanie.txt', 'w', encoding='utf8')
outFile2 = open('02Zadanie.txt', 'w', encoding='utf8')
outFile3 = open('03Zadanie.txt', 'w', encoding='utf8')
outFile4 = open('04Zadanie.txt', 'w', encoding='utf8')
outFile5 = open('05Zadanie.txt', 'w', encoding='utf8')
outFile6 = open('06Zadanie.txt', 'w', encoding='utf8')

df = pd.read_csv('titanic.csv', )
df['Pclass'] = df['Pclass'].astype(object)

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.

zadacha1 = df.groupby(['Sex'])['PassengerId'].count()
sex_counts = df['Sex'].value_counts()
print(f"На корабле ехало {sex_counts['male']} мужжин и {sex_counts['female']} женщин", file=outFile1)

# 2. Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. Ответ приведите в процентах (число в
# интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.

zadacha2 = df['Survived'].value_counts()
surv_percent = 100 * zadacha2[1] / zadacha2.sum()
print(f'Выжило {"{:0.2f}".format(surv_percent)}% пассажиров', file=outFile2)

# 3. Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах (число в
# интервале от 0 до 100, знак процента не нужен), округлив до двух знаков.

pclass_count = df['Pclass'].value_counts()
pclass_persent = 100 * pclass_count[1] / pclass_count.sum()
print("{:0.2f}".format(pclass_persent), file=outFile3)

# 4.Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два
#  числа через пробел.

age = df['Age'].dropna()
print(f'{"{:0.2f}".format(age.mean())}  {age.median()}', file=outFile4)

# 5.Коррелируют ли число братьев/сестер/супругов с числом родителей/детей? Посчитайте корреляцию Пирсона между
# признаками SibSp и Parch.

corr = df['SibSp'].corr(df['Parch'])
print("{:0.2f}".format(corr), file=outFile5)


# 6. Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name) его личное
# имя (First Name). Это задание — типичный пример того, с чем сталкивается специалист по анализу данных. Данные очень
#  разнородные и шумные, но из них требуется извлечь необходимую информацию. Попробуйте вручную разобрать несколько
# значений столбца Name и выработать правило для извлечения имен, а также разделения их на женские и мужские.

def clean_name(name):
    # Первое слово до запятой - фамилия
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)

    # Если есть скобки - то имя пассажира в них
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)

    # Удаляем обращения
    name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)

    # Берем первое оставшееся слово и удаляем кавычки
    name = name.split(' ')[0].replace('"', '')

    return name


names = df[df['Sex'] == 'female']['Name'].map(clean_name)
name_counts = names.value_counts()
print(name_counts.head(1).index.values[0], file=outFile6)

outFile1.close()
outFile2.close()
outFile3.close()
outFile4.close()
outFile5.close()
outFile6.close()
