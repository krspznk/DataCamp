# Importing modules
# ... YOUR CODE FOR TASK 1 ...
import pandas as pd
# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")

# Print out yearly
# ... YOUR CODE FOR TASK 1 ...
print(yearly)
# Calculate proportion of deaths per no. births
# ... YOUR CODE FOR TASK 2 ...
yearly["proportion_deaths"]=yearly["deaths"]/yearly["births"]
# Extract Clinic 1 data into clinic_1 and Clinic 2 data into clinic_2
clinic_1 = yearly[yearly["clinic"]=="clinic 1"]
clinic_2 = yearly[yearly["clinic"]=="clinic 2"]

# Print out clinic_1
# ... YOUR CODE FOR TASK 2 ...
print(clinic_1)
# Import matplotlib
...
# This makes plots appear in the notebook
import matplotlib.pyplot as plt

# Plot yearly proportion of deaths at the two clinics
# ... YOUR CODE FOR TASK 3 ...
ax=clinic_1.plot(x="year", y="proportion_deaths", label="clinic_1")
clinic_2.plot(x="year", y="proportion_deaths", ylabel="Proportion deaths", label="clinic_2", ax=ax)
# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv("datasets/monthly_deaths.csv", parse_dates=["date"])

# Calculate proportion of deaths per no. births
# ... YOUR CODE FOR TASK 4 ...
monthly["proportion_deaths"]=monthly["deaths"]/monthly["births"]
# Print out the first rows in monthly
# ... YOUR CODE FOR TASK 4 ...
print(monthly.head())
# Plot monthly proportion of deaths
# ... YOUR CODE FOR TASK 5 ...
ax=monthly.plot(x="date", y="proportion_deaths", ylabel="Proportion deaths")
# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly["date"]<handwashing_start]
after_washing = monthly[monthly["date"]>=handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
# ... YOUR CODE FOR TASK 6 ...
ax=before_washing.plot(x="date", y="proportion_deaths", label="before_washing")
after_washing.plot(x="date", y="proportion_deaths", label="after_washing", ax=ax, ylabel="Proportion deaths")
# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = after_proportion.mean() - before_proportion.mean()
print(mean_diff)
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append( (boot_after.mean()-boot_before.mean()))

# Calculating a 95% confidence interval from boot_mean_diff
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])

# The data Semmelweis collected points to that:
doctors_should_wash_their_hands = True