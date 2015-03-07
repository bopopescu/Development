import matplotlib.pyplot as pyplot
import numpy as np

def plotMe(x_array, y_array):
	f, plot_array = pyplot.subplots(2, sharex = True)
	plot_array[0].plot(x_array, y_array)
	plot_array[1].scatter(x_array, y_array)
	pyplot.show()


def evaluateModFunction(x):
	return ((x%6)**2)%7 - np.sin(x)
	

def evaluateMe(x):
	return -1 * x**4 + 1000 * x**3 -20 * x**2 + 4 * x + 6  

if __name__ == "__main__":
	start_number = int(raw_input("Enter the start of x values "))
	end_number = int(raw_input("enter the end of the x values "))
	y_array = []
	for i in xrange(start_number, end_number):
		y_array.append(evaluateModFunction(i))

	plotMe(range(start_number, end_number), y_array)