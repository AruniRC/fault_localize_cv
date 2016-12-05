#!/usr/bin/python

import pandas as pd
import numpy as np
import random

'''
	Basic skeleton code to create folds and display values.


'''


FILENAME = '../data/scores_artificial_vs_real.csv' # Path to fault_localization_data/.../
N_FOLDS = 5

# read in the CSV file as a Pandas DataFrame
df = pd.read_csv(FILENAME)
df.head()  # debug: check if the values look ok

# Handle non-unique Family values:
# 	The column "Formula" has the value "ochiai" repeated for the same Bug,
#	once with "Family=mbfl" and again with "Family=sbfl".
#	Hack: for rows "Family=sbfl","Formula=ochiai", rename "Formula=ochiai_s"
df.loc[(df.Formula == 'ochiai') & (df.Family == 'sbfl'), 'Formula'] \
	= 'ochiai_s'

# get unique elems in "Formula" column
formulaSet = list(set(df['Formula'].tolist()))

# create Cross-Validation folds as an extra column in the DataFrame
#	Within each Technique or Formula, get K splits of the bugs (rows)
df['Fold'] = np.nan
for fs in formulaSet:
	idx = (df['Formula'] == fs).tolist()

	# generate the K folds
	nData = len(idx)
	numRep = np.ceil(nData/N_FOLDS) + 1
	kFoldSet = range(1,N_FOLDS+1)
	kFolds = np.repeat(kFoldSet, numRep)
	if len(kFolds) > nData:
		kFolds = kFolds[0:nData]  # clip unequal lengths

	# random permutation on the fold values	
	random.seed(24)	
	random.shuffle(kFolds)

	# assign the fold values to all row with "Formula=fs"
	df.loc[idx, 'Fold'] = kFolds

# import pdb
# pdb.set_trace()

# get mean scores (ScoreWRTLoadedClasses) grouped by "Formula"
dfMeanScore = df.groupby('Formula')['ScoreWRTLoadedClasses'].mean()
print(dfMeanScore)

# mean scores for each fold
cvMeanScore = df.groupby(['Formula', 'Fold'])['ScoreWRTLoadedClasses'].mean()

# TODO - average and std dev over the folds.




