import code
import numbers
import threading
import time

import matplotlib.pyplot as plt
import numpy as np

def _checkIntegral(x):
	return isinstance(x, numbers.Number)

def setFunction(func, precision=100, domain=(-100, 100)):
	"""
	Set the plotted function.
	
	Parameters:
		func - The function f to be plotted.
		precision - The precision of graph (the number of points lie between neighboring integer).
	"""
	if not (type(precision) == int and precision > 0):
		raise Exception('precision {} is not a positive number.'.format(precision))
	
	if not (type(domain) == tuple and len(domain)==2 and all(_checkIntegral(x) for x in domain)) :
		raise Exception('domain {} is not valid.'.format(domain))
	
	devx, devy = [], []
	
	for i_int in range(*domain):
		for i_point in range(precision):
			x = i_int + (i_point / precision)
			try:
				xval, yval = x, func(x)
			
			except:
				pass
			
			else:
				devx.append(xval)
				devy.append(yval)
	
	plt.clf()
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('Plot of f(x)')
	
	plt.plot(devx, devy, label='f(x)')
	plt.legend()
	plt.draw()

def _initPlot():
	plt.ioff()
	
	setFunction(lambda x: x)
	plt.show()

def _interactiveShell():
	shell = code.InteractiveConsole({**globals(), **locals()})
	shell.interact()

_plotStarted = False
def startPlot():
	"""
	Start the plotting functions.
	
	Exceptions:
		Raises Exception if called more than once.
	"""
	global _plotStarted
	
	if _plotStarted:
		raise Exception('start() called more than once.')
	
	_plotStarted = True
	
	threading.Thread(target=_interactiveShell).start()
	_initPlot()