import code
import collections
import math
import numbers
import threading
import time
import warnings
from warnings import warn as _warn

import matplotlib.pyplot as plt
import numpy as np

class _FRange(collections.Sequence):
	# Mind that some methods have not been overriden yet, and the 
	# complexity of running them might be huge.
	
	__eps = 1e-9
	def __init__(self, src, dst, step=1, closed=False):
		self.__src = src
		self.__dst = dst
		self.__step = step
		
		self.__isClosed = closed
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if not len(self):
			raise StopIteration
		
		rep = self.__src
		self.__src += self.__step
		return rep
	
	def __len__(self):
		src, dst, step = self.__src, self.__dst, self.__step
		eps = _FRange.__eps
		
		dist = (dst - src) / step
		remain = math.floor(dist + eps)
		if not (not self.__isClosed and abs((src + remain*step) - dst) < eps):
			remain += 1
		
		return max(remain, 0)
	
	def __getitem__(self, k):
		return self.__src + __step*k

def viewRect(xlim=None, ylim=None):
	"""
	Get or set the limits of the XY axes.
	
	Optional Parameters:
		xlim - the new X limits.
		ylim - the new Y limits.
	
	Returns:
		xlim, ylim - the new XY axes.
	
	Remarks:
		Both parameters are optional, so call this function with
		no parameter to retrieve the axes.
	"""
	
	if xlim:
		plt.xlim(xlim)
	
	if ylim:
		plt.ylim(ylim)
	
	plt.draw()
	
	return dict(xlim=plt.xlim(), ylim=plt.ylim())

def _checkIntegral(x):
	return isinstance(x, numbers.Number)

def setFunction(func, domain=(-100, 100), precision=.01):
	"""
	Set the plotted function.
	
	Parameters:
		func - The function f to be plotted.
		
		Optional Parameters:
			domain    - The domain of the function as tuple (min_x, max_x).
			precision - The precision of graph (the length between
			            neighboring sampled point).
	"""
	isNumber = _checkIntegral
	frange = _FRange
	
	if not (isNumber(precision) and precision > 0):
		raise Exception('precision {} is not a positive number.'.format(precision))
	
	elif precision <= 1e-9:
		_warn('Precision less than 1e-9 migth have precision error.')
	
	if not (type(domain) == tuple and len(domain)==2 and all(isNumber(x) for x in domain)) :
		raise Exception('domain {} is not valid.'.format(domain))
	
	devx, devy = [], []
	
	for x in frange(*domain, precision):
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
	plt.gcf().canvas.set_window_title('plotGraph')
	
	setFunction(lambda x: x)
	plt.show()

def _latterJoinDict(*args):
	sumdict = {}
	for dct in args:
		for key in dct:
			sumdict[key] = dct[key]
	
	return sumdict

def _interactiveShell(extNames={}):
	shell = code.InteractiveConsole(_latterJoinDict(globals(), locals(), extNames))
	shell.interact()

_plotStarted = False
def startPlot(extNames={}):
	"""
	Start the plotting functions.
	
	Optional Parameters:
		extNames: Extra variables used in interaction.
	
	Exceptions:
		Raises Exception if called more than once.
	"""
	global _plotStarted
	
	if _plotStarted:
		raise Exception('startPlot() called more than once.')
	
	_plotStarted = True
	
	threading.Thread(target=_interactiveShell, args=(extNames,)).start()
	_initPlot()