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
import matplotlib.patheffects as pe
import matplotlib.dates as dt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Read the data
df = pd.read_excel("/Users/ardenott/Desktop/president_approval_polls.xlsx")

# Calculate the rolling average to smooth out data
rolling_mean_yes = df.yes.rolling(window=100).mean()
rolling_mean_no = df.no.rolling(window=100).mean()

# Adjust figure size
fig, ax = plt.subplots(figsize=(11,9.5), dpi=300)

# Plot all data points and rolling average line
plt.plot(df['end_date'], df['yes'], marker='o', linestyle=' ', alpha=.3, color='g', markersize=6)
plt.plot(df['end_date'], df['no'], marker='o', linestyle=' ', alpha=.3, color='orange', markersize=6)
plt.plot(df['end_date'], rolling_mean_yes, color='g',lw=5,
         path_effects=[pe.Stroke(linewidth=10, foreground='white'), pe.Normal()])
plt.plot(df['end_date'], rolling_mean_no, color='orange', lw=5,
         path_effects=[pe.Stroke(linewidth=10, foreground='white'), pe.Normal()])

# Reformat dates to enhance readability
date_form = dt.DateFormatter('%b %y')
ax.xaxis.set_major_formatter(date_form)
ax.tick_params(labelsize=15)

# Add gridlines
ax.xaxis.grid()
ax.yaxis.grid()

# Format and print graph
plt.title('Presidential Approval', size=40)
plt.ylabel('Approval in %', fontsize=20)
plt.legend(['Approve', 'Disapprove'], numpoints=50, fontsize=20)
plt.show()

