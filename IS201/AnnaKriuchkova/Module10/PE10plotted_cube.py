#import matlotlib
import matplotlib.pyplot as plt

#establish values to be plotted
x_values = range(1,6)
y_values = [x**3 for x in x_values]
print(y_values) - #[1,8,27,64,125] as shown in the hint

#customize and scatter the points
plt.scatter(x_values, y_values, c='Green', edgecolors='none', s=40)

#Set chart title and label axes
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#Set range for each axis
plt.axis([0, 10, 0, 150])

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Display the result
plt.show()