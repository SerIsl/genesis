import pandas as pd

def print_deco(function):
	def wrapper(x, y):
		bn = ',\n'
		count = 0
		a = function(x, y)
		print('[')
		for i in a:
			if count == len(a)-1:
				print(i, sep="", end="")
			else:
				print(i, sep="", end='')
				print(bn, sep='', end='')
				count +=1
		else:
			print('\n]')
	return wrapper	
