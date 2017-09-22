#Import requisite vizualization/statistics packages
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pandas import *
from numpy import *
matplotlib.style.use('ggplot')
%matplotlib inline

#Read in dataset
wfl = pd.read_csv('wfl.csv')
print "Done."

#Insert missing values
wfl = wfl.replace('na', np.NaN)
print "Done."

#Reset the index to the Team variable
wfl = wfl.set_index('Team')

#Convert string columns to numeric
wfl = wfl.apply(pd.to_numeric, errors='ignore')

#Analyze effect of tenure on performance
years = wfl.count(axis=1) #Count the year tenure of each team
performance = wfl.mean(axis=1) #Average rank per year involved
years_performance = pd.concat([years, performance], axis=1, join='inner') #Put that jank together
years_performance=years_performance.rename(columns = {0:'Years'})
years_performance=years_performance.rename(columns = {1:'Average_Rank'})
years_performance = years_performance.dropna() #Get rid of n00bs

#Graph
ax = years_performance.plot(x='Years', y='Average_Rank', kind='scatter', figsize=(17,8), color='b', s=50);
plt.ylabel('Average Rank');
plt.xlabel('Years in League');
plt.ylim((1,12))
plt.xlim((0,12))

#Add general regression line
x = years_performance['Years']
y = years_performance['Average_Rank']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"b--")

#Another way to do the regression
import statsmodels.api as sm
x = sm.add_constant(x)
est = sm.OLS(y, x).fit()
est.summary()

#Another way to do the regression
import statsmodels.formula.api as smf
est = smf.ols(formula='Average_Rank ~ Years', data=years_performance).fit()
est.summary()

#Apply regression formula to observed datapoints
years_performance['regression']=years_performance['Years']*-0.2969+8.0254

#Alternative regression plot
ax1 = years_performance.plot(x='Years', y='Average_Rank', kind='scatter', figsize=(17,8), c='b', s=50);
ax2 = years_performance.plot(kind='line', x='Years', figsize=(17,8), y='regression', color='r', ax=ax1)
plt.ylabel('Average Rank');
plt.xlabel('Years in League');
plt.ylim((1,12))
plt.xlim((0,12))

#Let's panel graph performance of all the teams in the dataset

#Set the number of graphs
graphs = 25

#adjust dataset to meet number of graphs
wfl_transpose = wfl.transpose().ix[:,0:graphs]

#create a list of positions for the chart
position = []
for i in range(5):
    for j in range(5):
        b = i,j
        position.append(b)

name_list= list(wfl_transpose)
        
#create base of subplot chart.. rows x columbs = graphs
fig, axes = plt.subplots(nrows=5, ncols=5, sharey=True, sharex=True, figsize=(6,6))
plt.ylim((0,12))
fig.subplots_adjust(hspace=.5)

#fill in base with graphs based off of position
for i in range(graphs):
            wfl_transpose.ix[:,i].plot(ax=axes[position[i]], kind='bar', color='r');
            axes[position[i]].set_title(name_list[i], size = 10);
            axes[position[i]].tick_params(labelsize=5)




