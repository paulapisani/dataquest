
# need way to visualize freq distributions for nominal / ordinal variables
wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()
wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh()
wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title='Blah')

# pie chart can sometimes be easier way to visualize relative frequencies
# can use figsize and autopct to help format (or remove labels)
wnba['Exp_ordinal'].value_counts().plot.pie()
wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%',
                                    title = 'Percentage of players in WNBA by level of experience')
plt.ylabel('')

# points is continuous interval / ratio variable, can be measured in more sophisticated ways
# histogram is good option here - grouping data into 10 bins for example, then finding frequencies
wnba['PTS'].plot.hist()

# can manually see what's going on under hood for bar chart
print(wnba['PTS'].value_counts(bins=10).sort_index())

from numpy import arange
wnba['PTS'].plot.hist(grid = True, xticks = arange(2,584,58.2), rot=30)
wnba['PTS'].describe()

# histogram is visual form of grouped frequency table
# also modified version of a bar plot
# main differences are that there are no gaps, and each bar represents an interval (end point of one bar = start of next)
# in ordinal bar charts, values aren't necessarily adjacent (so leave space between)

# looking again at histogram, there is tradeoff between number of intervals (info) and comprehensibility
# 10 is often good tradeoff between (can use bins parameter to change manually, can also specificy range)
wnba['Games Played'].plot.hist(range=(1,32), bins=8, title='The distribution of players by games played')
plt.xlabel('Games played')

# distributions can be skewed to right or left (depends on where body and tail of distributions are)
# left (negatively) skewed = tail on left side and body on right 
# right (positively) skewed = tail on right side and body on left
# symmetric = roughly equal on both sides (common example = normal, or Gaussian distribution)
# uniform = values distributed roughly uniformly across entire range 