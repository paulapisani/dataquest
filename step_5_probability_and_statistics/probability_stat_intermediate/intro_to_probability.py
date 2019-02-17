# start by showing country with flag that has most bars

print(flags[:2])

bars_ordered = flags['bars'].sort_values(ascending=False).head(1).index
most_bars_country = flags.iloc[bars_ordered]['name']


population_ordered = flags['population'].sort_values(ascending=False).head(1).index
highest_population_country = flags.iloc[population_ordered]['name']

# probability can be described as chance of event or sequence of events occurring
# coin flip example: two clear outcomes (heads / tails)
# in other cases, there are more than 2 outcomes

total_countries = flags.shape[0]

orange_probability = flags[flags['orange'] == 1].shape[0] / total_countries
stripe_probability = flags[flags['stripes'] > 1].shape[0] / total_countries

# conjunctive prob = probability involving sequence of events
# something happens, and then something else happens
# eg 5 coin flips --> prob of 5 heads --> 0.5 ^ 5

five_heads = .5 ** 5

ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100

# if we pick and remove with each pick, events are dependent (one event depends on the next)
# eg bag of 10 M&Ms --> 5 green, 5 blue --> prob of first blue = 1/2 (prob of blue = 4/9 after first draw though)

total_country = flags.shape[0]
total_red = flags[flags['red'] == 1].shape[0]

def prob_func(numerator, denominator, in_a_row):
    product = 1
    for i in range(in_a_row):
        product *= (numerator - i) / (denominator - i)
    return product 

three_red = prob_func(total_red, total_country, 3)

# sometimes want to know if probability of some event or another event occurring (eg rolling a 2 or a 3)

start = 1
end = 18000
def count_evenly_divisible(start, end, div):
    divisible = 0
    for i in range(start, end+1):
        if (i % div) == 0:
            divisible += 1
    return divisible

hundred_prob = count_evenly_divisible(start, end, 100) / end
seventy_prob = count_evenly_divisible(start, end, 70) / end

# common for events to not be mutually exclusive
# eg how many cars are red or SUVs - could add probability of each separately, but would overestimate if there was overlap

pr_stripes = flags[flags['stripes'] >= 1].shape[0] / flags.shape[0]
pr_bars = flags[flags['bars'] >= 1].shape[0] / flags.shape[0]
pr_stripes_and_bars = flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)].shape[0] / flags.shape[0]
stripes_or_bars = pr_stripes + pr_bars - pr_stripes_and_bars

pr_red = flags['red'].sum() / flags.shape[0]
pr_orange = flags['orange'].sum() / flags.shape[0]
pr_red_and_orange = flags[(flags['red'] == 1) & (flags['orange'] == 1)].shape[0] / flags.shape[0]
red_or_orange = pr_red + pr_orange - pr_red_and_orange

# in case of more than 2 conditions in or statement, need more robust approach
# one way to solve is find probability of everything that doesn't match criteria first, then subtract from 1 (100%)
# see below for prob of at least one head (1-prob of no heads)

heads_or = 1 - 0.5 ** 3
