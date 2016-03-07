# -*- coding: utf-8 -*-
import pandas

# Solution for A11--------------------------------------------------------------

df = pandas.read_csv('../data/result_part.csv')
group_megye_part_sum = df['szavazat'].groupby([df['megye'], df['part']]).sum()

def calculate_percent_megye(i):
    return 100 * i / float(i.sum())

result = group_megye_part_sum.groupby(level=0).apply(calculate_percent_megye)
print result


# Visualization-----------------------------------------------------------------

import matplotlib.pyplot as plt

# Simple examples
plt.plot([1, 2, 3, 4])
plt.show()

plt.plot([1, 2, 3, 5], label='my line')
plt.ylabel('some random numbers')
plt.title('My first python graph')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()

# plt.xkcd()

plt.plot([1, 2, 3, 5], 'ro', label='my points')
plt.ylabel('some random numbers')
plt.title('My first python graph')
plt.grid(True)
plt.legend(loc='upper left')
plt.savefig('myfig.png')  # save the actual figure as .png
plt.show()

means = [2, 10, 9]
groups = ['A', 'B', 'C']
errors = [3, 4, 2]
# alpha stands for transparency
plt.bar(range(len(means)), means, yerr=errors, align='center', alpha=0.5)
plt.xticks(range(len(means)), groups)
plt.axhline(0)  # horizontal line across the axis
plt.show()


# Use #1: draw functions
x = range(-100, 100)

def my_complicated_function(i):
    # With numpy you can use much more complicated constructs
    return i**4 - 367*i**3 + 1800*i**2 - 789*i + 654


y = [my_complicated_function(i) for i in x]

plt.plot(x, y, 'b--')
plt.show()


# Useful settings
import matplotlib
from matplotlib import rcParams, style
style.use('fivethirtyeight')
rcParams.update({'figure.autolayout': True})

# Use #2: visualize data
## Simple examples
def get_result_for_szk(megye, telepules, szk):
    return df[df.megye == megye][df.telepules == telepules][df.szavazokor == szk]

restricted_df = get_result_for_szk(1, 1, 1)

restricted_df.plot(kind='bar', x='part', y='szavazat', legend=False)
plt.show()

# Use percent results by counties
df_results = result.unstack('part')
print df_results.columns.values
df_results.plot(kind='scatter', x='FIDESZ-KDNP', y='JOBBIK')
plt.show()
df_results.plot(kind='scatter', x='MSZP-EGYÜTT-DK-PM-MLP', y='LMP')
plt.show()

interesting_partys = ['FIDESZ-KDNP', 'JOBBIK', 'LMP', 'MSZP-EGYÜTT-DK-PM-MLP']
colors = ['orange', 'blue', 'green', 'red']

restricted_results = df_results[interesting_partys]

restricted_results.plot(kind='bar', color=colors)
plt.legend(ncol=2)
plt.show()

restricted_results.plot(kind='hist', alpha=0.5, color=colors, bins=20)
plt.legend(ncol=2)
plt.show()
