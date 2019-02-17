# flow: collect data, analyze it, make use of analysis
# analyze for different puposes:
#	describe phenomena (science)
#	improve systems (engineering)
#	describe different aspects of society (data journalism)
# ability to understand data by looking at it in table format is limited (decreases with size)
# first type of aggregation that can be helpful is frequency distribution table

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wnba = pd.read_csv('wnba.csv')
print(wnba)

wnba_shape = wnba.shape
print(wnba_shape)

# pandas has value counts function that makes freq distr easy to create
# very effective for variables measured on nominal scale (eg position)
# 	have unique / different values, and no direction between

freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()

# above is less effective for height, which is measured on ratio scale
# in that case, may want to use .sort_index()

age_ascending = wnba['Age'].value_counts().sort_index(ascending=True)
age_descending = wnba['Age'].value_counts().sort_index(ascending=False)

# for ordinal, need to first create and then use another strategy to sort
# in this case, can't just use Ascending = True (alphabetical)
# instead use .iloc([indices in order])

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]
print(pts_ordinal_desc)

# value counts returns raw count, but often want to look at prop or percentage
# could divide by length of list but tedious
# instead use normalize and multiple by 100 to get to percentage

age_norm = wnba['Age'].value_counts(normalize=True).sort_index()
proportion_25 = age_norm[25]
percentage_30 = age_norm[30] * 100.0
percentage_over_30 = age_norm.loc[30:36].sum() * 100.0
percentage_below_23 = age_norm.loc[21:23].sum() * 100.0

# above is example of calulating percentile rank
# pcnt rank of value x in freq ditribution = percent of values that are less than or equal to x
# scipy.stats has percentileofscore(a, score, kind='weak' is good option

from scipy.stats import percentileofscore

percentile_rank_half_less = percentileofscore(wnba['Games Played'], 17, kind='weak')
percentage_half_more = 100 - percentile_rank_half_less

# Series.describe() method returns count, mean, std, min, 25/50/75th percentile, and max
# 25th, 50th, and 75th percentiles are called quartiles
# can use iloc to isolate specific outputs (eg. .describe().iloc[3:])
# can also use percentiles = parameter

percentiles = wnba['Age'].describe(percentiles=[0.5,0.75,0.95])
age_upper_quartile = percentiles['75%']
age_middle_quartile = percentiles['50%']
age_95th_percentile = percentiles['95%']

question1 = True
question2 = False
question3 = True

# sometimes frequency tables need to be bucketed to read clearly 
# can do this with value_counts(bins=x)
# called a group frequency distribution table
# each bin also nknown as a class interval

grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize=True).sort_index(ascending=False)*100.0

# clear trade off between how much info in table, and readability
# as number of class intervals increases, info increases but comprehensability decreases
# as rule of thumb, 10 class intervals is good tradeoff
# can manually set intervals as seen below

intervals = pd.interval_range(start = 0, end = 600, freq = 60)
gr_freq_table_10 = pd.Series([0,0,0,0,0,0,0,0,0,0], index=intervals)


for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval] += 1
            break

total = gr_freq_table_10.sum()






