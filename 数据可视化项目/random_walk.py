from random import choice

class RandomWalk():

    def __init__(self, number_points=5000):
        self.num_points = number_points

        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        # y_direction = choice([1, -1])
        # y_distance = choice([0, 1, 2, 3, 4])
        # y_step = y_direction * y_distance

        return x_step

    def fill_walk(self):

        while len(self.x_value) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)