import matplotlib.pyplot as plt

from random_walk import Walking_random

rw = Walking_random(50000)
rw.fill_walk()

plt.figure(dpi = 128 , figsize=(10,6))
# use the figure and dpifor the changing of the plot to involve all the elements are present  
point_numbers = list(range(rw.number_points))

plt.scatter(rw.x_values , rw.y_values , c=point_numbers , cmap=plt.cm.Purples ,
		edgecolor="none" ,   s=1)
# The first scatter is the starting point 
plt.scatter(0,0, c="green" , edgecolor="none" , s=5)
# the second scatter is the ending point
plt.scatter(rw.x_values[-1] , rw.y_values[-1] , c="red" , edgecolor="none", s=5)
# use the s for the dot size
plt.show()


