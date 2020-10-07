from random import choice

class Walking_random():

    def __init__(self, number_points = 5000):
        self.number_points = number_points

    # begin all values at 0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.number_points:
            x_directions = choice([1 , -1]) 
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_directions * x_distance # result would be two values, Which way and how far?

            y_directions = choice([1, -1]) 
            y_distance = choice([0, 1, 2, 3, 4]) 
            y_step = y_directions * y_distance # result would be two values, Which way and how far?

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

    # add the sums 
            self.x_values.append(next_x) 
            self.y_values.append(next_y)
