#scatter() function allows to plot a single point

import matplotlib.pyplot as plt 

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values, y_values, s=100) #accepts x & y coordinates of an individual point or series of points (if stored in a list)
#points are plotted one at a time

#Set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
