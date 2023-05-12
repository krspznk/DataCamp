# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
# ... YOUR CODE FOR TASK 1 ...

# Reading in the Nobel Prize data
nobel = pd.read_csv("datasets/nobel.csv")

# Taking a look at the first several winners
# ... YOUR CODE FOR TASK 1 ...
nobel.head(n=6)
# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
# ... YOUR CODE FOR TASK 2 ...
display(len(nobel))
# Display the number of prizes won by male and female recipients.
# ... YOUR CODE FOR TASK 2 ...
display(nobel["sex"].value_counts())
# Display the number of prizes won by the top 10 nationalities.
# ... YOUR CODE FOR TASK 2 ...
nobel["birth_country"].value_counts().head(n=10)
# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel["birth_country"]=="United States of America"
nobel['decade'] = np.floor(nobel["year"]/100).astype("int64")
prop_usa_winners = nobel.groupby("decade", as_index=False)["usa_born_winner"].mean()
# # Display the proportions of USA born winners per decade
# # ... YOUR CODE FOR TASK 3 ...
display(prop_usa_winners)
# Setting the plotting theme
sns.set()
# and setting the size of all plots.
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners
ax = sns.lineplot(data=prop_usa_winners, x="decade", y="usa_born_winner")

# Adding %-formatting to the y-axis
from matplotlib.ticker import PercentFormatter
# ... YOUR CODE FOR TASK 4 ...
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel["sex"]=="Female"
prop_female_winners = nobel.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

# ... YOUR CODE FOR TASK 5 ...
ax = sns.lineplot(data=prop_female_winners, x="decade", y="female_winner", hue="category")
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
# Picking out the first woman to win a Nobel Prize
# ... YOUR CODE FOR TASK 5 ...
nobel[nobel["sex"]=="Female"].nsmallest(1, "year")
# Selecting the laureates that have received 2 or more prizes.
# ... YOUR CODE FOR TASK 5 ...
nobel.groupby("full_name").filter(lambda group: len(group)>=2)
# Converting birth_date from String to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year']-nobel['birth_date'].dt.year

# Plotting the age of Nobel Prize winners
sns.lmplot(data=nobel, x="year", y="age", lowess=True, aspect=2, line_kws={'color' : 'black'})
# Same plot as above, but separate plots for each type of Nobel Prize
# ... YOUR CODE FOR TASK 9 ...
sns.lmplot(data=nobel, x="year", y="age", lowess=True, aspect=2, line_kws={'color' : 'black'}, row="category")
# The oldest winner of a Nobel Prize as of 2016
# ... YOUR CODE FOR TASK 10 ...
display(nobel.nlargest(1, "age"))
# The youngest winner of a Nobel Prize as of 2016
# ... YOUR CODE FOR TASK 10 ...
nobel.nsmallest(1, "age")
youngest_winner = 'Malala Yousafzai'
