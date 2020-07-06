import pandas as pd
import numpy as np
import sys
import os
from processing import Processor
from utils import submit
from sklearn import linear_model

if __name__ == '__main__':
	train = pd.read_csv("data/train.csv")
	test = pd.read_csv("data/test.csv")

	process = Processor()

	processed_train, processed_test = process.pre_process(train, test)

	X_train = processed_train.loc[:, processed_train.columns != 'SalePrice'].values
	Y_train = processed_train.loc[:, processed_train.columns == 'SalePrice'].values
	X_test = processed_test.loc[:, processed_test.columns != 'SalePrice'].values

	reg = linear_model.LassoLars(max_iter=100, alpha=.1)
	reg.fit(X_train, Y_train)

	y_hat = reg.predict(X_test)
	submit(y_hat)


