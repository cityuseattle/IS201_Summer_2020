import matplotlib.pyplot as plt 

multi = [0,5,10,15,20,25,30]
plt.style.use('seaborn')   #set background style
fig, ax = plt.subplots() #subplots() generates one+ plots in the same figure
#fig - collection of plots; ax - single plot

ax.plot(multi, linewidth=5) #linewidth determines the thickness of a plotted line

#Set chart title and label axes
ax.set_title('Multiple of 5', fontsize=24) 
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Multi Values', fontsize=14)

#Set size of tick labels
ax.tick_params(axis = 'both', labelsize=14) #axis = 'both' affects tick marks on both axes

plt.show() #display the plot