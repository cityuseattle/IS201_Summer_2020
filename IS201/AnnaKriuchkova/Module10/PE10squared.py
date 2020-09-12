#import matplotlib
import matplotlib.pyplot as plt 

#establish values to be plotted
x_values = range(1,11)
y_values = [x**2 for x in x_values]
print(y_values) #[1,4,9,16,25,36,49,64,81,100] as shown in the hint

#customize and scatter the points
plt.scatter(x_values, y_values, c='blue', edgecolors='none', s=40)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set range for each axis
plt.axis([0, 12, 0, 120])

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Display the result
plt.show()