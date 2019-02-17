# sometimes want to compare multiple distributions at once using frequency tables
# seaborn countplot gives good option here with grouped bar plot

sns.countplot(x='Exp_ordinal', hue='Pos', data=wnba, 
              order=['Rookie','Little experience','Experienced','Very experienced','Veteran'],
              hue_order=['C','F','F/C','G','G/F'])

wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')
sns.countplot(x='age_mean_relative', hue='min_mean_relative', data=wnba)

# hard to see overlapping distributions and not very granular in above
# can see larger overlapping distributions using histtype = 'step'

wnba[wnba.Age >= 27]['MIN'].plot.hist(label='Old', legend=True, histtype='step')
wnba[wnba.Age < 27]['MIN'].plot.hist(label='Young', legend=True, histtype='step')
plt.axvline(wnba.MIN.mean(), label='Average')
plt.legend()

# even easier to see shape of distribution with kernal density estimate plot
# abbreviated to kde - these plots display densities (prob values) rather than frequencies

wnba[wnba.Age >= 27]['MIN'].plot.kde(label='Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label='Young', legend=True)
plt.axvline(wnba.MIN.mean(), label='Average')
plt.legend()

# kde becomes less useful once you have 5+ distributions
# first alternative is called a strip plot
# each strip is unique x axis value, while y axis value is distirbution of points
# can add jitter to increase readability

sns.stripplot(x='Pos', y='Weight', data=wnba, jitter=True)

# boxplot could be more informative in some cases (doesn't show individual points though)
# sometimes called box and whisker due to lines extending to max and min
# if data point is greater than 1.5xIQR, flagged as outlier (can change using whis param)

sns.boxplot(x='Pos', y='Weight', data=wnba)
sns.boxplot(wnba[wnba['Pos'] == 'C']['Height'], whis = 4,
           orient = 'vertical', width = .15)

sns.boxplot(wnba['Games Played'])
iqr = 7.0
lower_bound = 22.0 - (iqr*1.5)
upper_bound = 29.0 + (iqr*1.5)
outliers_low = wnba[wnba['Games Played'] < lower_bound]['Games Played'].count()
outliers_high = wnba[wnba['Games Played'] > upper_bound]['Games Played'].count()