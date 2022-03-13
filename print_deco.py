

def print_deco(function):
	def wrapper(x, z):
		bn = ',\n'
		count = 0
		a = function(x, z)
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
