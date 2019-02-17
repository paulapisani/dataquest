# binomial probability distribution --> 2 values that add up to 1, 100% odds of one of two outcomes happening
# many common events can be expressed this way (eg coin flip, winning game, stock market going up)
# often interested in chance of certain outcome happening in a sequence
# core component of these different tests is binomial distribution

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = bikes[bikes['cnt'] >= 5000].shape[0] / bikes.shape[0]

# can formalize full binomial probability in function

import math
outcome_counts = list(range(31))

def binomial_prob(N, k, p):
    orderings = math.factorial(N) / (math.factorial(k) * math.factorial(N-k))
    probability = (p ** k) * ((1-p) ** (N-k))
    return probability * orderings

outcome_probs = []
for i in outcome_counts:
    outcome_probs.append(binomial_prob(30,i,0.39))

# can plot this as bar chart

import matplotlib.pyplot as plt

plt.bar(outcome_counts, outcome_probs)
plt.show()

# probability mass function from scipy - will give probabilities of each k in outcome_counts list
# binomial distribution only needs two parameters (N = total number of events, p = probability of outcome we're interested in seeing)
# pmf scipy function takes in list of outcomes, total number of events, and probability of outcome we're interested in seeing

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31) # creating a bunch of different k values
outcome_probs = binom.pmf(outcome_counts, 30, 0.39)

plt.bar(outcome_counts, outcome_probs)

# voiceover for probability distribution function: if we repeatedly look at samples, the expected number of outcomes will follow this distribution
# tells us which values are likely, and how likely they are
# expected value = N * p, standard deviation = sqrt(N * p * q)

N = 30
p = 0.39
q = 1-p
dist_stdev = math.sqrt(N * p * q)
dist_mean = N * p

# can show how binomial distribution changes as N increases

from scipy import linspace
from scipy.stats import binom

plt.subplot(1,2,1)
outcome_counts_10 = linspace(0,10,11)
outcome_probs_10 = binom.pmf(outcome_counts_10, 10, 0.39)
plt.bar(outcome_counts_10, outcome_probs_10)

plt.subplot(1,2,2)
outcome_counts_100 = linspace(0,100,101)
outcome_probs_100 = binom.pmf(outcome_counts_100, 100, 0.39)
plt.bar(outcome_counts_100, outcome_probs_100)

# distribution gets narrower as N increases --> moves closer to normal distribution
# alternative to probability density function is cumulative density function
# in cumulative, for each k, we fill in probability that k outcomes or less occur (should be 1 by end of outcome set)
# can you binom.cdf (instead of .pmf)

outcome_counts = linspace(0,30,31)
outcome_probs = binom.cdf(outcome_counts, 30, 0.39)
plt.plot(outcome_counts, outcome_probs)

# can again use z score here to find percentage of values to left or right of values we're looking at
# every normal distributoin has same percentage of data that's within certain number of std mean 
# can use standard normal table to see that ~68% of data is within 1 std, ~95% within 2, ~99% within 3
# mu = N*p, sigma = sqrt(N*p*q), z-score = (k-mu) / sigma
# eg 16 days out of 30 with 5000+ riders --> z = (16 - (30*0.39)) / sqrt(30*0.39*0.61) --> 4.3 / 2.67 = 1.61 std
# distance btw mean and 1.61 std above is ~ 44.63% of data (89.26% if including below also)
# ~5.37% chance of observing value that is 1.61 std or more above mean (same percent 1.61+ std below)

left_16 = binom.cdf(16,30,0.39)
right_16 = 1-left_16

# cdf above is quick way to calculate probability to left of particular value (including)
# left = binom.cdf(k, N, p), right = 1-left
# cdf won't return exact value that z-score does, because distribution isn't exactly normal
# gives actual amount of prob in a distribution to left of given k








