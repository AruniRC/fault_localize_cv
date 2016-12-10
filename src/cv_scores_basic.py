#!/usr/bin/python

import pandas as pd
import numpy as np
import random

'''
	Basic skeleton code to create folds and display values.
'''


FILENAME = '../data/scores_artificial_vs_real_with_indicator.csv' # Path to fault_localization_data/.../
N_FOLDS = 5

# read in the CSV file as a Pandas DataFrame
df = pd.read_csv(FILENAME)
#print(df.head())  # debug: check if the values look ok

# Handle non-unique Family values:
# 	The column "Formula" has the value "ochiai" repeated for the same Bug,
#	once with "Family=mbfl" and again with "Family=sbfl".
#	Hack: for rows "Family=sbfl","Formula=ochiai", rename "Formula=ochiai_s"
df.loc[(df.Formula == 'ochiai') & (df.Family == 'sbfl'), 'Formula'] \
	= 'ochiai_s'
df.loc[(df.Formula == 'ochiai') & (df.Family == 'mbfl'), 'Formula'] \
	= 'ochiai_m'


# create Cross-Validation folds as an extra column in the DataFrame
# projectSet = list(set(df['Project'].tolist()))
projectSet = df.Project.unique()
df['Fold'] = np.nan
cvMeanScore = []
for fs in projectSet:
	
	# select all other projects - Leave One Project Out
	df['Fold'] = np.nan
	df.at[df['Project'] != fs,'Fold'] = fs
	
	# mean scores for each project
	cvMeanScore = df.groupby(['Fold', 'isReal', 'Formula'])['ScoreWRTLoadedClasses'].describe()
	cvMeanScore.to_csv('results/cv_result'+fs+'.csv', sep=',', header=True, index=True)
