import matplotlib.pyplot as plt

numbers_on_y = [1 , 4 , 9 , 16 , 25]
numbers_on_x = [1, 2, 3, 4, 5]

# use the linewidth to control the thickness of the scale
plt.plot(numbers_on_x , numbers_on_y, linewidth = 1)

# use the title to name your program, font size is controlled by fontsize
plt.title("Testing the matplotlib", fontsize = 24)

# use xlabel to name the x-axis of your program
plt.xlabel("Value", fontsize = 14)

# use ylabel to name the y-axis of your program
plt.ylabel("Squares of Value" , fontsize = 14)

# controls the numbers that appear on the x-axis and y-axis
plt.tick_params(axis="both" , labelsize = 14)


# Display the results
plt.show()
