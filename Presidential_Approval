'''
    I'm using matplotlib and pandas to create a chart showing the presidential
    approval rating over time. Since the data can be quite noisy, I calculated
    the rolling average to generate a smooth line so that the data can be better
    visualized. The data came from FiveThirtyEight's poll collection and is
    inspired by the work they do. To test the code, the data set can be
    downloaded here:
    https://projects.fivethirtyeight.com/polls-page/president_approval_polls.csv
    Just be sure to save the file as a .xlsx, not .csv.
'''


import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters


register_matplotlib_converters()
# Read the data
df = pd.read_excel("/Users/ardenott/Desktop/president_approval_polls.xlsx")

# Calculate the rolling average to smooth out data
rolling_mean_yes = df.yes.rolling(window=100).mean()
rolling_mean_no = df.no.rolling(window=100).mean()

# Plot all data points and rolling average line
plt.scatter(df['end_date'], df['yes'], alpha=.02, color='g')
plt.scatter(df['end_date'], df['no'], alpha=.02, color='orange')
plt.plot(df['end_date'], rolling_mean_yes, color='g', lw=3)
plt.plot(df['end_date'], rolling_mean_no, color='orange', lw=3)

# Format and print graph
plt.title('Presidential Approval', size=20)
plt.ylabel('Approval in %')
plt.legend(['Approve', 'Disapprove'])
plt.show()

