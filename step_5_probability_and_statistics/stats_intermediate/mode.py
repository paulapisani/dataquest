# mean takes into account each value in distribution - and easy to define algebraically
# superior to median, but median helpful in cases when mean not possible / appropriate
# also cases where mean and median both unsuitable

houses = pd.read_csv('AmesHousing_1.txt',sep='\t')

houses['Land Slope'].head(20)
scale_land = 'ordinal'

houses['Roof Style'].head(20)
scale_roof = 'nominal'

houses['Kitchen AbvGr'].head(20)
kitchen_variable = 'discrete'

# median doesn't make a whole lot of sense in case of ordinal variable in case where middle values are different (len = even)
# instead could use most frequent value - called the mode

def mode_func(array):
    tracker = {}
    for value in array:
        if value in tracker:
            tracker[value] += 1 
        else:
            tracker[value] = 1
    return max(tracker, key=tracker.get)

mode_function = mode_func(houses['Land Slope'])
mode_method = houses['Land Slope'].mode()
same = mode_function == mode_method

# roof style is particularly good candidate for mode (since it's nominal not ordinal)

def mode_func(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return (max(counts, key = counts.get), counts)

mode, value_counts = mode_func(houses['Roof Style'])

# there are cases where mean / median are possible, but mode is preferable
# good example: kitchen above ground 
# mean is 1.04, median is 1, but but mode is safer for non-technical audience (easiest to make sense of)

bedroom_variable = 'discrete'
bedroom_mode = houses['Bedroom AbvGr'].mode()

price_variable = 'continuous'
price_mode = houses['SalePrice'].mode()

# some distributions have multiple modes (bimodal = 2) while others have only one (unimodal)
# usually specific to continuous variables - workaround there is grouped frequency table
# this method has limitations, but good start

intervals = pd.interval_range(start=0, end=800000, freq=100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index=intervals)

for value in houses['SalePrice']:
	for interval in intervals:
		if value in interval:
			gr_freq_table.loc[interval] += 1
			break

max_count = 0
max_mid_interval = 0
for interval in gr_freq_table.index.unique():
    count = gr_freq_table.loc[interval]
    mid_interval = (interval.left + interval.right) / 2
    if count >= max_count:
        max_count = count
        max_mid_interval = mid_interval

mode = max_mid_interval
median = houses['SalePrice'].median()
mean = houses['SalePrice'].mean()

sentence_1 = True
sentence_2 = True

# some general patterns for median vs mean vs mode
# for right skewed distribution, usually have mode < median (slightly to right of mode) < mean
# for left skewed distributions, usually have mean < median < mode

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(), houses['SalePrice'].max()))

plt.axvline(150000, color = 'Green', label = 'Mode')
plt.axvline(houses['SalePrice'].median(), color = 'Black', label = 'Median')
plt.axvline(houses['SalePrice'].mean(), color = 'Orange', label = 'Mean')
plt.legend()

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1 = 'right skew'
shape_2 = 'right skew'
shape_3 = 'left skew'

# in perfectly symmetric distribution, all three would fall in same spot
# possible to have symmetric multimodal distribution, where mean = median, but mode is elsewhere
# uniform distribution has no mode (all equal probability)

import matplotlib.pyplot as plt

houses['Mo Sold'].plot.kde(xlim=[1,12])
plt.axvline(houses['Mo Sold'].mode()[0], color='Green', label='Mode')
plt.axvline(houses['Mo Sold'].median(), color='Orange', label='Median')
plt.axvline(houses['Mo Sold'].mean(), color='Black', label='Mean')
plt.legend()

# summary: mode ideal for ordinal data represented with words, nominal data, discrete data (comm to non-technical audience)
# position of mean, median, mode is predictable based on skew and symmetry
#




