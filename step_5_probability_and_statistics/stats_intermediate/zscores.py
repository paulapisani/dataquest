# key question: is randomly sampled observation high, low, or roughly average compared to distribution of values?
# answer depends on standard deviation of distribution

import pandas as pd
import matplotlib.pyplot as plt

houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim=(min(houses['SalePrice']),max(houses['SalePrice'])))
plt.axvline(houses['SalePrice'].mean(), color='Black', label='Mean')
plt.axvline(houses['SalePrice'].mean()+houses['SalePrice'].std(ddof=0), color='Red', label='Standard deviation')
plt.axvline(220000, color='Orange', label='220000')
plt.legend()

# process above is visual check, but not very scalable - need faster / more precise way to measure how far value is from mean
# can measure distance from mean in terms of number of standard deviations (more stds --> farther away)

price = 220000
mean_pop = houses['SalePrice'].mean()
std_pop = houses['SalePrice'].std(ddof=0)
st_devs_away = (price - mean_pop) / std_pop

# process here is finding distance between value and mean, then dividing by standard deviation of distribution
# z score = (x - mu) / sigma --> x is observed value, sigma is standard deviation
# represents number of standard deviations away from mean
# z score for sample is same, but with Bessel's correction --> z = (x - xbar) / s
# z scores can be both positive and negative depending on whether value is above or below mean (z score has sign and value)
# even for positive z scores, usually written out as +x to clarify

import numpy

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def zscore_func(value, array):
    sample_mean = sum(array) / len(array)
    sample_std = numpy.std(array, ddof=0)
    return (value - sample_mean) / sample_std

min_z = zscore_func(min_val, houses['SalePrice'])
max_z = zscore_func(max_val, houses['SalePrice'])
mean_z = zscore_func(mean_val, houses['SalePrice'])

# can find zscore for same value across different distributions

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

neighborhoods = {'NAmes':'North Ames', 'CollgCr':'College Creek', 'OldTown':'Old Town', 'Edwards':'Edwards', 'Somerst':'Somerset'}
zscores = {}
for hood in neighborhoods:
    filtered_sample = houses[houses['Neighborhood'] == hood]
    zscores[hood] = abs(z_score(200000, filtered_sample['SalePrice']))

best_investment = neighborhoods[min(zscores, key=zscores.get)]

# can convert values for specific series to z scores, then plot via kde
# for every distribution of z scores, mean should be ~0 and stdev should be ~1
# this is also known as a standard distribution (with standard scores) --> have standardized the distribution

mean_pop_price = houses['SalePrice'].mean()
std_pop_price = houses['SalePrice'].std(ddof=0)

houses['z_prices'] = houses['SalePrice'].apply(lambda x: (x-mean_pop_price) / std_pop_price)
z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof=0)

plt.figure(figsize = (11,7))
plt.subplot(2,2,1)
houses['z_prices'].plot.kde(color='Black', label='Price')
plt.subplot(2,2,2)
houses['SalePrice'].plot.kde(color='Black', label='Price')



mean_pop_area = houses['Lot Area'].mean()
mean_std_area = houses['Lot Area'].std(ddof=0)

houses['z_areas'] = houses['Lot Area'].apply(lambda x: (x-mean_pop_area) / mean_std_area)
z_mean_area = houses['z_areas'].mean()
z_stdev_area = houses['z_areas'].std(ddof=0)

plt.subplot(2,2,3)
houses['z_areas'].plot.kde(color='Black', label='Lot Area')
plt.subplot(2,2,4)
houses['Lot Area'].plot.kde(color='Black', label='Lot Area')

plt.legend()
plt.tight_layout()

# follow up example of standardizing population
# mu z = mean of distribution of z scores --> mu z = (mu - mu) / sigma = 0 for any mu
# sigma z = std of distribution of z scores --> sigma z = ((mu + sigma) - mu) / sigma = sigma / sigma = 1 for any sigma

from numpy import std, mean
population = [0,8,0,8]

pop_mean = sum(population) / len(population)
pop_std = numpy.std(population, ddof=0)

population_standardized = []
for i in population:
    z_score = (i - pop_mean) / pop_std
    population_standardized.append(z_score)

mean_z = sum(population_standardized) / len(population_standardized)
stdev_z = numpy.std(population_standardized, ddof=0)

# can do the same as the above with samples (just need to change ddof to 1)
# here, mean of standardized sample is still 0 in sample, but std of standardized sample is not (if ddof=0 used)
# after standardizing sample, resulting distribution of z-scores is itself a sample
# when ddof=1 used, then stdev = 1 for sample

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = numpy.std(standardized_sample, ddof=1)

# standardizing distributions useful to compare values coming from different measurement systems 
# steps: standardize each distribution of index values (transform to z score), then compare z scores
# assumptions here --> full distributions show up in each dataset being compared

pop_mean_index1 = houses['index_1'].mean()
pop_std_index1 = houses['index_1'].std(ddof=0)
houses['index_1_standardized'] = houses['index_1'].apply(lambda x: (x-pop_mean_index1) / pop_std_index1)

pop_mean_index2 = houses['index_2'].mean()
pop_std_index2 = houses['index_2'].std(ddof=0)
houses['index_2_standardized'] = houses['index_2'].apply(lambda x: (x-pop_mean_index2) / pop_std_index2)

print(houses[['index_1_standardized','index_2_standardized']].head())
better = 'first'

# challenge: z scores not always straightforward to work with / communicate to non-tech audiences
# can convert z scores back to values that are more intuitive
# z = (x - mu) / sigma --> x = z * sigma + mu
# this conversion preserves location of z score, and allows for any choice of mu and sigma 
# can convert back to original distribution by using original mu and sigma

houses['z_unmerged'] = houses['z_merged'].apply(lambda x: (x*10)+50)
mean_transformed = houses['z_unmerged'].mean()
stdev_transformed = houses['z_unmerged'].std(ddof=0)
