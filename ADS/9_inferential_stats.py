import pandas as pd
population = pd.read_csv('diamonds.csv')
# has cols like carat, cut, color, clarity, depth, table, price, x, y, z
sample = population.sample(n=40)

# metrics for formula
sample_mean = sample['price'].mean()
# is 3104

sample_std_deviation = sample['price'].std()
population_mean = population['price'].mean()
population_std_deviation = population['price'].std()


# H0: Average price of diamonds is 3200
# HA: Average price of diamonds is not 3200

# Z-test
import math 
Z = (sample_mean-population_mean)/(population_std_deviation/math.sqrt(40))
# Z = -1.3131 

critical_value = +-1.64
# Z lies between critical value, hence do not reject H0

# T-test
sample = population.sample(20)
sample_mean = sample['price'].mean()
sample_std_deviation = sample['price'].std()

t_stat = (sample_mean-population_mean)/(sample_std_deviation/math.sqrt(20))
# t_stat = -1.151
# t_statistic < t_table we reject null hypothesis

# z test when pop size > 30  and t test will be when  pop size<30
