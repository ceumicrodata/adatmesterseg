import pandas

s = pandas.Series([1, 2, 3])
print s

data = {'part': ['fidesz', 'jobbik'], 'szavazat': [60, 40]}
frame = pandas.DataFrame(data)

print frame

df = pandas.read_csv('ass9-sample.csv')
print df.head()

print df[:100]

print df['part']
print df['szavazat']

df['uj'] = 'NaN'

print df.tail()

df['szavazat'] = df['szavazat'].str.strip(' ')

new = df[df['megye'] == 1][df['telepules'] == 1][df['szavazokor'] == 1]
print df[df.megye == 1][df.telepules == 1][df.szavazokor == 1]
print new
