# focus for this section: deeper statistical techniques / metrics \
# (eg std dev, z scores, confidence intervals, prob. estimation, hypothesis testing)

# steps: get good data, understand how it's structured, organize the data, visualize patterns (organize>summarize>visualize)

# sampling - often want to use subset of data to answer questions about larger dataset
# population = set of all relevant individuals
# sample = subset of full population
# same group can be both a population and a sample depending on question

# in ideal world, we'd use full population to answer every question (not always possible though)
# when taking a sample, it's by definition incomplete so there will always be some amount of error
# sampling error = difference between metric for population and metric for sample
# parameter = metric specific to population
# statistic = metric specific to sample
# sampling error = parameter - statistic

import pandas as pd
wnba = pd.read_csv('wnba.csv') 

print(wnba.head())
print(wnba.tail())
print(wnba.shape)

parameter = wnba.loc[:,'Games Played']
sample = parameter.sample(random_state=1)
statistic = max(sample)
sampling_error = max(parameter)-statistic

# goal is for sample statistic to get as close to population parameter as possible
# need individuals in sample to be similar to population in order for this to happen
# eg sampling from basketball teams vs US general pop, expect larve sampling error
# want our samples to be representative
# one approach is giving every individaul in population equal chance to be selected 
# in order to do so, we need to sample randomly
# simple random sample (SRS) - generate random numbers to select sample units
# use of random_state variable makes generation of random numbers predictable
# series.sample() uses pseudorandom number generator
# pseudorandom uses initial value to generate sequence similar in properties to true random
# this is important in scientific research where reproducibility is important

import pandas as pd
import matplotlib.pyplot as plt

sample_means = []
wnba = pd.read_csv('wnba.csv')
wnba_mean = wnba['PTS'].mean()
for n in range(100): 
    sample = wnba.loc[:,'PTS'].sample(10,random_state=n)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)

plt.scatter(range(1,101),sample_means)
plt.axhline(wnba_mean)

# in example above, sample means can vary quite a bit from population mean
# likely because sample is not very representative
# can address this by increasing sample size
# observations: 
# 	simple random sample not reliable when sample size is small
# 	large sample size is important for accuracy (decreases chances of unrepresentative sample)

# simple random sampling can leave out certain population individuals that are important to us
# eg from above is player position
# to ensure we end up with players from each position, we can sample from subgroups
# stratified sampling = break population into smaller groups and then use SRS 
# stratum = each group in stratified sampling

wnba['pts_per_game'] = wnba['PTS'] / wnba['Games Played']
pts_per_game_by_pos = {}
for position in wnba['Pos'].unique():
    stratum = wnba[wnba['Pos'] == position]
    sample = stratum['pts_per_game'].sample(10, random_state=0)
    sample_mean = sample.mean()
    pts_per_game_by_pos[position] = sample_mean
position_most_points = max(pts_per_game_by_pos, key=pts_per_game_by_pos.get)

# in case of total points scored, depends on number of games played
# 72% of wnba players played 22+ games
# when randomly sampling here, we may end up with sample that skews significantly differently
# one solution is using stratified sampling while bing mindful of proportions in population
# in this case, stratify by some characteristic then randomly sample proportional # of obs

print(wnba['Games Played'].min())
print(wnba['Games Played'].max())
print(wnba['Games Played'].value_counts(bins=3, normalize=True) * 100)
pop_mean = wnba['PTS'].mean()

stratum_1 = wnba[wnba['Games Played'] <= 12]
stratum_2 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
stratum_3 = wnba[wnba['Games Played'] > 22]

sampling_means = []
for n in range(100):
    sample_1 = stratum_1['PTS'].sample(1, random_state=n)
    sample_2 = stratum_2['PTS'].sample(2, random_state=n)
    sample_3 = stratum_3['PTS'].sample(7, random_state=n)
    combined_sample = pd.concat([sample_1, sample_2, sample_3])
    combined_mean = combined_sample.mean() 
    sampling_means.append(combined_mean)

plt.scatter(range(1,101),sampling_means)
plt.axhline(pop_mean)

# the above strategy of proportional sratified sampling isn't much better than SRS
# poor performance is due to choice of strata
# number of games played isn't as strong as something like minutes played
# guidelines for choosing good strata:
# 	minimize variability within each stratum (player with 500 vs. 5 pts in same stratum)
#		in this case, want either more granular stratification or different criterion
#	maximize variability between strata
#		strata should be different from one another
#	stratification criterion should be correlated with property we want to measure

print(wnba['Team'].unique())
print(pd.Series(wnba['Team'].unique()).sample(4, random_state=0))
team_sample = list(pd.Series(wnba['Team'].unique()).sample(4, random_state=0))
team_sample_filtered = wnba[wnba['Team'].isin(team_sample)]

stat_height = team_sample_filtered['Height'].mean()
stat_age = team_sample_filtered['Age'].mean()
stat_bmi = team_sample_filtered['BMI'].mean()
stat_total_pts = team_sample_filtered['PTS'].mean()

pop_height = wnba['Height'].mean()
pop_age = wnba['Age'].mean()
pop_bmi = wnba['BMI'].mean()
pop_total_pts = wnba['PTS'].mean()

sampling_error_height = pop_height - stat_height
sampling_error_age =  pop_age - stat_age
sampling_error_BMI =  pop_bmi - stat_bmi
sampling_error_points = pop_total_pts - stat_total_pts

#	can do descriptive statistics (describe population or sample) or inferential statistics
























