import pandas as pd
import numpy as np
import sys
import os

class Processor:
	def __init__(self):
		pass

	def pre_process(self, train, test):
		X_train = train.iloc[:, :]
		Y_train = train.iloc[:, -1].values

		X_test = test.iloc[:, :]

		df = pd.concat([X_train, X_test], ignore_index=True)

		df = pd.get_dummies(df.iloc[:, :])
		locations = set((np.where(np.isnan(df) == True))[1])

		for i in (locations):
			nan_locations = np.isnan(df.values[:, i])
			(df.iloc[:, i]).loc[nan_locations] = 0

		processed_train = df.loc[np.where(df['SalePrice'].values != 0)]
		processed_test = df.loc[np.where(df['SalePrice'].values == 0)]

		return processed_train, processed_test

	def post_process(self):
		pass
