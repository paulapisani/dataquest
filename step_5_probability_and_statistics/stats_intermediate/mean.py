# several ways to summarize data with single value (mean, weighted mean, median, mode)
# can also measure variability with variance and std deviation
# can use z score to locate value in a distribution

distribution = [0,2,3,3,3,4,13]
mean = sum(distribution)/len(distribution) 
center = (13-0)/2 == mean

distance_above = 0
distance_below = 0
for i in distribution:
    if i > mean:
        distance_above += i - mean 
    else:
        distance_below += mean - i

equal_distances = distance_above == distance_below

# notes about mean above -- sum of distance from every point above equals distance from every point velow
# not necessarily in the center of the range (can think about weight being balanced on scale)

from numpy.random import randint, seed 

equal_distances = 0
for i in range(5000): 
	seed(i)
	distr = numpy.random.randint(0,1000,10)
	mean = sum(distr)/len(distr) 
	distance_above = 0
	distance_below = 0
	for j in distr:
		if j > mean:
			distance_above += j-mean
		else: 
			distance_below += mean-j
	if round(distance_below, 1) == round(distance_above, 1):
		equal_distances += 1

# mu is used for population mean, with observations x1 through xn (divided by capital N for total size of population)
# xbar is sample mean (divided by lowercase n for sample population size) - several other names including M, Xbar, xbar n

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def mean_func(array):
    total = 0
    n = len(array)
    for value in array:
        total += value
    return total / n

mean_1 = mean_func(distribution_1)
mean_2 = mean_func(distribution_2)
mean_3 = mean_func(distribution_3)

# can use pandas to compute mean (rather than calculating by hand)

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()
means_are_equal = function_mean == pandas_mean

# can take random samples of different size to see how sampling error decreases as n increases
# generally see sample error decrease as n increases, but not always the case

mean = houses['SalePrice'].mean()

x_val = []
y_val = []
for i in range(101):
    num = 5 + i*29
    sample = houses['SalePrice'].sample(num, random_state=i)
    sample_mean = sample.mean()
    sample_error = mean - sample_mean
    x_val.append(num)
    y_val.append(sample_error)

plt.scatter(x_val, y_val)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

# distribution of sample means centers around mean and gets tighter as n, or samle size, increases (less variance)

means = []

for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state=i)
    means.append(sample.mean())

plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)

# when statistic is on average equal to parameter being estimated, it's said to be unbiased
# sample mean is unbiased estimator for population mean when sampling with or without replacement















