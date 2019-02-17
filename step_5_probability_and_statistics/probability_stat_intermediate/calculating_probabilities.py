# intro to probability for new dataset

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

total_days = bikes.shape[0]

days_over_threshold = bikes[bikes["cnt"] > 2000].shape[0]
probability_over_2000 = days_over_threshold / total_days

days_over_threshold_4000 = bikes[bikes['cnt'] > 4000].shape[0]
probability_over_4000 = days_over_threshold_4000 / total_days

# want to know prob of getting 2 or more heads if we flip 2 coins
# prob of 3 heads is easy, but prob of 2 out of 3 heads is tougher
# three possible combos --> HHT, HTH, THH
# each of these combos has a probability of 0.5 ** 3 = 0.125 --> 3*0.125 = 0.375 as final prob

coin_1_prob = 3*(0.5 ** 3)

# SNNNN, NSNNN, NNSNN, NNNSN, NNNNS --> 5 total

sunny_1_combinations = 5 * (0.7 ** 1) * (0.3 ** 4)

# can calculate number of combinations in which outcome can occur k times in set of N events 
# need to use factorial here
# formula --> N! / [ k! (N-k)! ]
# eg # of combos where 4 out of 5 days are sunny --> N = 5, k = 4 --> 5! / (4! * (5-4)!) --> 5! / 4! = 5

import math
def find_outcome_combinations(N, k):
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    return numerator / denominator

combinations_7 = find_outcome_combinations(10, 7)
combinations_8 = find_outcome_combinations(10, 8)
combinations_9 = find_outcome_combinations(10, 9)

# p = prob of sunny, q = prob not sunny --> as example of binomial distribution 
# eg prob of 4 days sunny out of 5 --> (0.7 ** 4) * (0.3 ** 1)
# prob = p ^ k * q ^ (N-k)

p = .6
q = .4

def prob_func(sunny_days):
    non_sunny_days = 10-sunny_days
    orderings = math.factorial(10) / (math.factorial(sunny_days) * math.factorial(non_sunny_days))
    return orderings * (p ** sunny_days) * (q ** non_sunny_days)

prob_8 = prob_func(8)
prob_9 = prob_func(9)
prob_10 = prob_func(10)

# eg situation --> have device that purportedly can make weather sunny
# observe that out of 10 days, there were 8 that were sunny 
# this event (8+ total sunny days) would happen ~17% of the time randomly 
# connecting back to statistical significance, 5% is common threshold -- so result above isn't statistically significant
