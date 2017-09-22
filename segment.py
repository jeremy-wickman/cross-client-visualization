#import standard packages
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#set style of graphing outputs
matplotlib.style.use('seaborn-darkgrid')
%matplotlib inline
print "Done."


#GET SOURCE DATA
#""" select
#                                    customer_id,
#                                    demographic_income,
#                                    client_survey,
#                                    weight,
#                                    her_totalrecall,
#                                    her_read_collapse,
#                                    her_read_thorough,
#                                    her_share_eeaction,
#                                    her_reception_liking,
#                                    her_reception_motivate,
#                                    sentiment_satisfaction11pt
#                                    from
#                                        X
#                                    """)

#Parse list of variables
variable_list1 = list(segment_dataset)

#Replace "missing values" in each variable
for i in variable_list1:
    segment_dataset[i] = segment_dataset[i].replace('99.0',np.NaN)
    
#Create groupings by demographic
for i in variable_list1:
    segment_dataset_grouped = segment_dataset.groupby(['demographic_education'])[variable_list1].agg(['mean', 'count'])

#New list of variables in grouped table
variable_list = list(segment_dataset_grouped.columns.levels[0])

#SEGEMENT PERFORMANCE BY OVERALL
print segment_dataset_grouped

#Visualize segment performance BY OVERALL
#Set the number of graphs
graphs = len(variable_list)

#create a list of positions for the chart
position = []
for i in range(3):
    for j in range(3):
        b = i,j
        position.append(b)

#Create base of subplot chart.. rows x columbs = graphs
fig, axes = plt.subplots(nrows=3, ncols=3, sharey=False, sharex=False, figsize=(6,6))
fig.subplots_adjust(hspace=.5)

#Fill in base with graphs based off of position
for i in range(graphs):
    segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='r')

#Set the formatting elements of the axes for each graph
for i in range(graphs):
    axes[position[i]].set_title(variable_list[i], size = 6)
    axes[position[i]].tick_params(labelsize=5)
    axes[position[i]].set_xlabel("demographics", size = 5)

#Set the appropriate y axis for each chart
for i in range(graphs):
    if segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()<1:
        axes[position[i]].set_ylim((0,1))
    elif 1< segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean() <5:
        axes[position[i]].set_ylim((1,5))
    elif segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()>5:
        axes[position[i]].set_ylim((1,11))
    else:
        pass
        
#Group the initial dataset into client_survey and demographics
segment_dataset_client = segment_dataset.groupby(['client_survey','demographic_education'])[variable_list1].agg(['mean', 'count'])
segment_dataset_client[:5]

#Visualize segment performance by both OVERALL and CLIENT_SURVEY average
#Set the number of graphs
graphs = len(variable_list)

#create a list of positions for the chart
position = []
for i in range(3):
    for j in range(3):
        b = i,j
        position.append(b)

#Create base of subplot chart.. rows x columbs = graphs
fig, axes = plt.subplots(nrows=3, ncols=3, sharey=False, sharex=False, figsize=(6,6))
fig.subplots_adjust(hspace=.5)

#Fill in base with graphs based off of position
for i in range(graphs):
    segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='r')

#Set the formatting elements of the axes for each graph
for i in range(graphs):
    axes[position[i]].set_title(variable_list[i], size = 6)
    axes[position[i]].tick_params(labelsize=5)
    axes[position[i]].set_xlabel("demographics", size = 5)

#Set the appropriate y axis for each chart
for i in range(graphs):
    if segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()<1:
        axes[position[i]].set_ylim((0,1))
    elif 1< segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean() <5:
        axes[position[i]].set_ylim((1,5))
    elif segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()>5:
        axes[position[i]].set_ylim((1,11))
    else:
        pass

#Add the results by client_survey average
for i in range(graphs):
    segment_dataset_client.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='b')

#Create weighted client_survey dataset

variable_list2 = list(segment_dataset)
variable_list2.remove('demographic_education')
variable_list2

segment_dataset_weighted = segment_dataset*1
for i in variable_list2:
    if np.issubdtype(segment_dataset_weighted[i].dtype, np.number) == True:
        segment_dataset_weighted[i]=segment_dataset['weight']*segment_dataset_weighted[i]
    else:
        pass

#Group the weighted dataset into client_survey and demographics
segment_dataset_weighted_client = segment_dataset_weighted.groupby(['client_survey','demographic_education'])[variable_list1].agg(['mean', 'count'])

#Take the weighted mean of the demographic level
segment_dataset_weighted_client = segment_dataset_weighted_client.mean(level=1)

#Visualize segment performance by both OVERALL and CLIENT_SURVEY average
#Set the number of graphs
graphs = len(variable_list)

#create a list of positions for the chart
position = []
for i in range(3):
    for j in range(3):
        b = i,j
        position.append(b)

#Create base of subplot chart.. rows x columbs = graphs
fig, axes = plt.subplots(nrows=3, ncols=3, sharey=False, sharex=False, figsize=(6,6))
fig.subplots_adjust(hspace=.5)

#Fill in base with graphs based off of position
for i in range(graphs):
    segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='r')

#Set the formatting elements of the axes for each graph
for i in range(graphs):
    axes[position[i]].set_title(variable_list[i], size = 6)
    axes[position[i]].tick_params(labelsize=5)
    axes[position[i]].set_xlabel("demographics", size = 5)

#Set the appropriate y axis for each chart
for i in range(graphs):
    if segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()<1:
        axes[position[i]].set_ylim((0,1))
    elif 1< segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean() <5:
        axes[position[i]].set_ylim((1,5))
    elif segment_dataset_grouped.xs(variable_list[i], level=0, axis=1)['mean'].mean()>5:
        axes[position[i]].set_ylim((1,11))
    else:
        pass

#Add the results by client_survey average

for i in range(graphs):
    segment_dataset_client.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='b')
for i in range(graphs):
    segment_dataset_weighted_client.xs(variable_list[i], level=0, axis=1)['mean'].plot(ax=axes[position[i]], kind='line', color='g')