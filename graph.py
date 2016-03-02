import matplotlib.pyplot as plt
import numpy as np
import time

class rt_2D_graph:
	
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)

		# some X and Y data
		self.x = np.arange(100)
		self.y = np.random.randn(100)
		plt.ylim(-500, 500)
		plt.xlim(0, 100)

		self.li, = self.ax.plot(self.x, self.y)

		# draw and show it
		self.fig.canvas.draw()
		plt.show(block=False)


	def update(self,new_value):
		self.y[:-1] = self.y[1:]
        	self.y[-1:] = new_value

		# set the new data
	        self.li.set_ydata(self.y)

	        self.fig.canvas.draw()
