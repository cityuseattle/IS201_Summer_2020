import matplotlib.pyplot as plt
#pyplot module contains functions to help in generating charts and plots

#if input_values are not provided, plot() sets the first data point of x-coordinate at 0 by default
input_values = [1,2,3,4,5]
squares = [1,4,9,6,25]
plt.plot(input_values, squares, linewidth = 5) #linewidth parameter controls thickness of a generated line

#Set chart title and label axes
plt.title('Square Numbers', fontsize=24) #title() function sets a chart title; fontsize parameter controls text size
plt.xlabel('Value', fontsize=14) #xlabel function sets a title for x axis
plt.ylabel('Square of Value', fontsize=14) #ylabel function sets a title for y axis

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()

