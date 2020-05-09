import matplotlib.pyplot as plt
import numpy as np

import threading, time

# plot_data = {'devx'=[], 'devy'=[], 'lock'=threading.Lock()}
plot_data = type('PlotData', (object,), dict(devx=[], devy=[], lock=threading.Lock())) ( )

def setFunction(func):
	with plot_data.lock:
		plot_data.devx = plot_data.devy = []
		
		for i in range(-100, 100):
			plot_data.devx.append(i)
			plot_data.devy.append(func(i))

def startPlot():
	plt.ion()
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('Plot of f(x)')
	
	setFunction(lambda x: x)
	
	plt.show()
	while True:
		with plot_data.lock:
			plt.clf()
			plt.plot(plot_data.devx, plot_data.devy, label='f(x)')
		
		plt.draw()
		plt.pause(0.01)
		time.sleep(0.01)
	
	plt.close()

def main():
	threading.Thread(target=startPlot).start()

if __name__=="__main__":
	main()