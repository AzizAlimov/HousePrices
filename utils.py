import sys
import os

def submit(y_hat):
	with open('data/submission1.csv', 'w') as f:
		f.write('id,SalePrice\n')
		for row in enumerate(y_hat):
			f.write('{0},{1}\n'.format(*(row[0]+1461, row[1])))