# new sales price table instead has average sales price with different frequencies by year
# could just avg mean price column, but wouldn't accurately reflect population
# need what's called the weighted mean here

total_sales = 0
total_houses = 0
for year in houses_per_year:
    n = houses_per_year['Houses Sold']
    sales = n * houses_per_year['Mean Price']
    total_sales += sales
    total_houses += n

weighted_mean = total_sales / total_houses
mean_original = houses['SalePrice'].mean()
difference = mean_original - weighted_mean

# numpy has weighted mean function (need to specify weights)

def weighted_mean(values, weights):
    total_value = 0
    total_weight = 0
    for i in range(len(values)):
        total_value += values[i] * weights[i]
        total_weight += weights[i]
    return total_value / total_weight

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])
weighted_mean_numpy = numpy.average(houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold'])
equal = weighted_mean_function == weighted_mean_numpy

# mean doesn't work in cases where distribution is open ended (eg 10 or more)
# common workaround is to sort all values in ascending order and then select middle value

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

# to find median value of even number of itesm, average two middle values 
# average is not restricted to mean (though often mean the same thing)
# median doesn't have standard notation, and has no neat way to define algebraically

replace_copy = houses['TotRms AbvGrd'].copy().replace({'10 or more': 10}).astype(int).sort_values(ascending=True)

length = len(replace_copy)
cutoff = int(length / 2)

if len(replace_copy) % 2 == 0:
    median = (replace_copy.iloc[cutoff] + replace_copy.iloc[cutoff+1]) / 2

# median only considers middle values - said to be robust to outliers
# mean is not robust to outliers

houses['Lot Area'].plot.box()
houses['SalePrice'].plot.box()

saleprice_difference = houses['SalePrice'].mean() - houses['SalePrice'].median() 
lotarea_difference = houses['Lot Area'].mean() - houses['Lot Area'].median()

# can theoretically use mean for coded variables but it's contentious
# argument against - mean assumes that measurement is on interval scale (levels could be somewhat arbitrary)
# example: 1-10 encoding vs 0-9 encoding for same scale - 8 / 4 vs. 7 / 3 gives different values
# argument for - still have to take average in case of median(so just as arbitrary)

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

plt.hist(houses['Overall Cond'])
more_representative = 'mean'

# in many cases, despite theoretical hurdles, mean is preferred because it's richer in information
# eg [1,1,1,2,2,2,2,3,3,3] vs. [1,2,2,2,2,2,4,5,5,5] --> mean shifted up, but median wouldn't show anything here
