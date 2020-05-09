import matplotlib.pyplot as plt
import numpy as np

import threading, time
import code

def setFunction(func):
	"""
	Set the plotted function.
	
	Parameters:
		func - The function f to be plotted.
	"""
	devx, devy = [], []
	
	for i_int in range(-100, 100):
		precision = 100
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