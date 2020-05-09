import matplotlib.pyplot as plt
import numpy as np

import threading, time
import code

def setFunction(func):
	""" Set the plotted function.
	
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

def main():
	""" Start the plotting functions.
	Raises exception if called more than once.
	"""
	def startPlot():
		plt.ioff()
		
		setFunction(lambda x: x)
		plt.show()
	
	def interactiveShell():
		shell = code.InteractiveConsole({**globals(), **locals()})
		shell.interact()
	
	threading.Thread(target=interactiveShell).start()
	startPlot()

if __name__=="__main__":
	main()