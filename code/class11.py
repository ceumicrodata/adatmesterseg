import pandas

s = pandas.Series([1, 2, 3])
print s

data = {'part': ['fidesz', 'jobbik'], 'szavazat': [60, 40]}
frame = pandas.DataFrame(data)

print frame

df = pandas.read_csv('../data/result_part.csv')
print df.head()

print df[:100]

print df['part']
print df['szavazat']

df['uj'] = 'NaN'

print df.tail()

new = df[df['megye'] == 1][df['telepules'] == 1][df['szavazokor'] == 1]
print df[df.megye == 1][df.telepules == 1][df.szavazokor == 1]
print new

print df.describe()
print df.drop_duplicates()

print df['part'].unique()

print df.groupby('part').mean()
group_megye_part = df['szavazat'].groupby([df['part'], df['megye']]).mean()
print group_megye_part.mean()
print group_megye_part.sum()
print group_megye_part.min()
print group_megye_part.median()
