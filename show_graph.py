import matplotlib.pyplot as plt
import numpy as np

import threading, time
import code

plot_data = type('PlotData', (object,), dict(devx=[], devy=[], needRedraw=False, lock=threading.Lock())) ( )
shell_exit = False

def setFunction(func):
	with plot_data.lock:
		plot_data.devx, plot_data.devy = [], []
		plot_data.needRedraw = True
		
		# for i in range(-100, 100):
		for i_int in range(-100, 100):
			precision = 100
			for i_point in range(precision):
				x = i_int + (i_point / precision)
				# print('#', x)
				try:
					xval, yval = x, func(x)
				
				except:
					pass
				
				else:
					plot_data.devx.append(xval)
					plot_data.devy.append(yval)
					# print('#', xval, yval)
					
				# print('#', i, func(i))
		
		plt.clf()
		plt.plot(plot_data.devx, plot_data.devy, label='f(x)')
		plt.draw()
		# plt.pause(0.01)

def startPlot():
	plt.ioff()
	
	setFunction(lambda x: x)
	
	plt.show()
	# while not shell_exit:
		# if plot_data.needRedraw:
			# with plot_data.lock:
				# plt.cla()
				
				# plt.xlabel('x')
				# plt.ylabel('f(x)')
				# plt.title('Plot of f(x)')
				
				# plt.plot(plot_data.devx, plot_data.devy, label='f(x)')
				# plt.draw()
				
				# plot_data.needRedraw = False
		
		# plt.pause(0.01)
		# time.sleep(0.01)
		# print('Now updating.', shell_exit)
	
	# plt.close()

def interactiveShell():
	global shell_exit
	
	shell = code.InteractiveConsole({**globals(), **locals()})
	shell.interact()
	
	# print('Well, trying to close...')
	shell_exit = True

def main():
	threading.Thread(target=interactiveShell).start()
	startPlot()

if __name__=="__main__":
	main()