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
