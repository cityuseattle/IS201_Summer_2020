import matplotlib.pyplot as plt 

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor = 'none', s=40)
#specified cmap colors points with lower y-values light blue, with larger - dark blue
#edgecolor removes outlines around points (prevents outlines from blending in)
#Note: for c, may define color (c='red'); 
#      may also define custom colors, by passing a 3-value RGB tuple (red-green-blue); 
#      value range: 0 to 1 (closer to 0 - darker, closer to 1 - lighter)
#      Example: c=(0,0,0.8) -> light blue dots 

#Colormap: a series of colors in a gradient that moves from a starting to ending color 
#Used to emphasize patterns in a given data

#Note: default color for points is blue with a black outline

#Set chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Set range for each axis
plt.axis([0, 1100, 0, 1100000]) 
#axis() function requires four values: min and max values for each of the axis

plt.savefig('squares_plot.png', bbox_inches='tight')
#plt.savefig() automatically saves the chart
#bbox_inches = 'tight': trims extra whitespace from the plot

import webbrowser
webbrowser.open('http://matplotlib.org/') #Examples -> Color Examples -> colormaps_reference
