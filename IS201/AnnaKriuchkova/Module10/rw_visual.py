import matplotlib.pyplot as plt 

from random_walk_txtb import RandomWalk

#Keep making new walks, as long as a program is active
while True:
    #Make a random walk and plot the points
    rw = RandomWalk(50000) #increasing the number of points
    rw.fill_walk()

    #Set the size of a plotting window
    plt.figure(dpi=100, figsize=(10,6)) #tuple gives dimensions of the plotting window in inches!
    #figure() function controls the width, height, resolution, and background color of the plot

    #Python assumes screen resolution = 80 pixels per inch; can pass dpi if know your screen's resolution

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    #Emphasize the first and last points
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
