import matplotlib.pyplot as plt

from random_walk import  RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_number = list(range(rw.num_points))
    # plt.scatter(rw.x_value, rw.y_value, c=point_number, cmap=plt.cm.Blues, edgecolors='none',s=1)
    plt.plot(rw.x_value, rw.y_value , linewidth=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("想继续吗宝贝？")
    if keep_running == 'q':
        break
