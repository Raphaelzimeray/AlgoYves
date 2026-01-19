from point import *
import matplotlib.pyplot as plt
import numpy as np

list_point = []

p1 = Point(3, 4, 'p1', 4, 'red')
p1.set_x(5)
list_point.append(p1)

list_point.append(Point(5, 5, 'p2', 6, 'orange'))


# point_1 = Point(3, 4, 'p1', 4, 'red')

# point_2 = Point(5, 5, 'p2', 6, 'orange')

for point in list_point:
    print(point)
    print("distance du point p1 à l'origine", point.norme())
    plt.scatter(point.get_x(), point.y, label = point.name, color = [point.color], s = 10 * point.weight ** 2)

p1.rotate(np.pi/8)
plt.scatter(p1.get_x(), p1.y, label = p1.name, color = [p1.color], s = 10 * p1.weight ** 2)


# plt.scatter(point_1.x, point_1.y, label = point_1.name, color = [point_1.color], s = 10 * point_1.weight ** 2)

# plt.scatter(point_2.x, point_2.y, label = point_2.name, color = [point_2.color], s = 10 * point_2.weight ** 2)

plt.legend()

plt.xlim(0, 10)

plt.ylim(0, 10)

plt.grid(True)

plt.xticks(np.arange(0, 11, 1))

plt.yticks(np.arange(0, 11, 1))

plt.xlabel('X')

plt.ylabel('Y')

plt.show()
