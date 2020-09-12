import matplotlib.pyplot as plt 
squares = [1,4,9,16,25]
fig, ax = plt.subplots() #needs two variables, since two subplots() returns two values \
                                                 #(fig for figure layout; ax for axes)
#ax = plt.subplots() causes line below to return AttributeError: 'tuple' object has no attribute 'plot'
ax.plot(squares)
plt.show()

import webbrowser
webbrowser.open('https://www.geeksforgeeks.org/matplotlib-pyplot-subplots-in-python/')
