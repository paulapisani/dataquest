# focus in this lesson is hypothesis testing and statistical signficiance
# hypothesis is pattern / rule about a process in world that can be tested
# can use hypothesis testing to determine if a chance we made had meaningful impact or not
# eg did new banner on website drive meaningful drop in user engagement
# eg does new weight loss pill helped people lose more weight

# hypothesis testing allows us to calculate the probability that random chance was actually responsible for diffeence in outcome
# every process has some inherent amount of randomness - understanding role of chance helps make right conclusion
# step 1: set up null hypothesis that describes status quo
# step 2: then state alternative hypothesis, which we use to compare with null hypothesis 
# step 3: decide which describes data better - either reject null hypothesis and accept alternative or vice versa

# more on pill example above: group of people split up into two groups, A and B
# A is given placebo while B is given actual pill, both groups told not to change anything else (this is called blind experiment)
# understanding research design for study is important first step that informs rest of analysis
# weight loss pill example is known as experimental study (participants brought together, given instructions, and observed)
# key part of experimental study is random assignment, to address bias
# flaws in research design can lead to wrong conclusions

# goal #1: use statistics to determine if difference in weight loss between 2 groups is bc of random chance or not
# want to explore data for two groups

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

plt.hist(weight_lost_a, label='A')
plt.hist(weight_lost_b, label='B')
plt.legend()

# need to frame hypotheses more quantitatively
# first step is to decide on test statistic - numerical value that summarizes the data
# want to know if amount of weight lost between groups is meaningfully different, so will use difference in means
# x bar denotes sample mean --> so null hypthosis: x bar b - x bar a = 0, alternative hypothesis: x bar b - x bar a > 0

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

# now we have test statistic, but need to decide on statistical test
# goal here is to decide liklihood that result we achieved was due to random chance

# one option is permutation test - involves simulating rerunning study many times and recalculating test statistic for each iteration
# rerunning means lumping groups a and b together and sampling from full distribution
# this helps us calculate a distribution of test statistics over many trials (called sampling distribution) and approximates full range of possibilities under null hypothesis
# can then benchmark observed test statistic
# want to see how common observed mean difference above is under null hypothesis 
# to simulate rerunning study, we randomly assign each data point to either group A or B
# keep track of recalculated test statistics as separate list
# in ideal world, number of times we re-randomize groups that each data point belongs to matches total number of possible permutations
# this is usually a very very large number and too high for computers to calculate in reasonable timeframe
# instead set iteration count -- tradeoff between accuracy and speed

import numpy as np
import matplotlib.pyplot as plt

mean_difference = 2.52
print(all_values)

mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        indicator = np.random.rand()
        if indicator >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)

# exercise above has helped us account for effect of random chance
# used bar chart to visualize, but can also use dictionary containing values so we can benchmark observed test statistic against it
# process is looping over values in mean_difference and counting frequency
# can use dict.get() method to return value at specified key if it exists, or return anoher value specified (default = False)
# eg empty = {} --> key_a = empty.get('a', False) --> will return false

sampling_distribution = {}
for mean_diff in mean_differences:
    if sampling_distribution.get(mean_diff,False):
        val = sampling_distribution.get(mean_diff)
        inc = val + 1 
        sampling_distribution[mean_diff] = inc 
    else:
        sampling_distribution[mean_diff] = 1

# now want to see number of times that a value of 2.52 (observed diff in mean) occurred in simulations 
# can then divide that by 1000 (total trials) to get p value, probability of observing mean diff of 2.52 due to random chance
# if p value is high, that means the mean diff could easily have happened randomly, and pill probably didn't do anything
# if p value is low, that means liklihood of observed difference happening by chance is unlikey 
# good practice to set up p-value threshold before conducting the study 
# then, if p value is less than threshold, then we reject null hypothesis and accept alternative (vice versa if p value is above)
# most common threshold is 0.05 --> somewhat arbitrary, but most researchers comfortable with it

frequencies = []
for key in sampling_distribution:
    if key >= 2.52:
        frequencies.append(sampling_distribution[key])

p_value = numpy.sum(frequencies) / 1000

# if you set p-value threshold too high (eg 10% rather than 5%), run the risk of Type 1 error (incorrectly rejecting null)
# if you set p-value threshold too low (eg 1% rather than 5%), run the risk of Type 2 error (incorrectly accepting null)












