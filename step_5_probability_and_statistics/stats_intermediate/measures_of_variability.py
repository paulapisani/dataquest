# take example of [4,4,4,4] vs. [0,8,0,8]
# mean and median are the same but don't reflect significant differences in variation
# first option is range (max - min)

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def range_func(array):
    return max(array) - min(array)

range_by_year = {}
for year in houses['Yr Sold'].unique():
    filtered_houses = houses[houses['Yr Sold'] == year]
    range_value = range_func(filtered_houses['SalePrice'])
    range_by_year[year] = range_value

# range only considers two (potentially extreme) values - eg [1,1,1,1,1,1,1,1,21]
# alternative - choose a reference value, then measure distance between each value and mean (then find the avg of distances)
# formula: sum(i to n of xi - mu) / N = average distance

C = [1,1,1,1,1,1,1,1,1,21]

mean_val = sum(C) / len(C)

def avg_dist(array):
    distances = []
    for i in array:
        distances.append(i-mean_val)
    return sum(distances) / len(distances)

avg_distance = avg_dist(C)
print(avg_distance)

# in example above, we have both positive and negative differences
# summing togetehr cancels out, so instead need alternative, like taking abolute value
# revising formula, get mean absolute deviation (or average absolute deviation)

C = [1,1,1,1,1,1,1,1,1,21]

mean = sum(C) / len(C)
def mean_abs_dev(array):
    distances = []
    for i in array:
        distances.append(abs(i - mean))
    return sum(distances) / len(distances)

mad = mean_abs_dev(C)

# another alternative here is taking mean squared distance or mean squared deviation instead (variance)
# this is also known as variance (equal to mad if there's no variation)

C = [1,1,1,1,1,1,1,1,1,21]

mean = sum(C) / len(C)
def var_func(array):
    sq_dist = []
    for i in array:
        sq_dist.append((i-mean)**2)
    return sum(sq_dist) / len(sq_dist)

variance_C = var_func(C)

# variance is tough to interpret because it's in units squared
# standard deviation is square root of variance (and in proper / interpretable units)

C = [1,1,1,1,1,1,1,1,1,21]

mean = sum(C) / len(C)
def var_func(array):
    sq_dist = []
    for i in array:
        sq_dist.append((i-mean)**2)
    return sum(sq_dist) / len(sq_dist)

variance_C = var_func(C)

# standard deviation is prob most used measure of variability
# tells us how much values in distribution vary on avg around the mean

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

std_per_year = {}
for year in houses['Yr Sold'].unique():
    houses_filtered = houses[houses['Yr Sold'] == year]
    std_year = standard_deviation(houses_filtered['SalePrice'])
    std_per_year[year] = std_year

greatest_variability = max(std_per_year, key=std_per_year.get)
lowest_variability = min(std_per_year, key=std_per_year.get)

# standard deviation can also be thought of as measure of spread

mean = houses['SalePrice'].mean()
st_dev = standard_deviation(houses['SalePrice'])
houses['SalePrice'].plot.hist()
plt.axvline(mean, color = 'Black', label = 'Mean')
plt.axvline(mean - st_dev, color = 'Red', label = 'Below')
plt.axvline(mean + st_dev, color = 'Violet', label = 'Above')
plt.legend()

# can sample repeatedly to see if standard deviation is unbiased estimator
# sample standard deviation usually underestimates population standard deviation
# think of population vs. sample --> intuitively more variation across larger spread

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

sample_stds = []
for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state=i)
    sample_std = standard_deviation(sample)
    sample_stds.append(sample_std)

plt.hist(sample_stds)
plt.axvline(standard_deviation(houses['SalePrice']))

# can correct bias above with Bessel's correction (dividing by n-1 instead of n)

from math import sqrt

def standard_deviation(array):
    mean = sum(array) / len(array)
    sq_dist = []
    for i in array:
        sq_dist.append((i-mean)**2)
    return sqrt(sum(sq_dist) / (len(sq_dist) - 1))

sample_stds = []
for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state=i)
    sample_std = standard_deviation(sample)
    sample_stds.append(sample_std)
    
plt.hist(sample_stds)
plt.axvline(standard_deviation(houses['SalePrice']))

# could add further currecting factor (n-2 for example) but need single mathematical definition
# lowercase sigma is used to describe population standard deviation (sq for population variance)
# lowercase s is used to describe sample standard deviation (sq for sample variance)
# numpy and pandas both have std and var functions with ddof parameter (default = 1 for n-1)

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample.std(ddof=1)
numpy_stdev = numpy.std(houses['SalePrice'], ddof=1)
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample.var(ddof=1)
numpy_var = numpy.std(houses['SalePrice'], ddof=1)
equal_vars = pandas_var == numpy_var

# primary arument for n-1 is that it makes sample variance unbiased estimator for population var
# this is only true when sampling with replacement
# eg [0,3,6] --> pop variance = 6
# take all possible combinations of n=2 samples
# take mean variance and mean stdev and compare to those for pop (ddof = 0)

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

sample_stds = []
sample_vars = []
for sample in samples:
    sample_stds.append(numpy.std(sample, ddof=1))
    sample_vars.append(numpy.var(sample, ddof=1))

equal_stdev = sum(sample_stds)/len(sample_stds) == numpy.std(population, ddof=0)
equal_var = sum(sample_vars)/len(sample_vars) == numpy.var(population, ddof=0)


























