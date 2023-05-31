
import matplotlib.pyplot as plt
points = [(666.6666666666667, -195.0), (506.6666666666667, -350.88457268119896), (186.66666666666669, -350.88457268119896),
          (26.66666666666667, -195.0), (186.66666666666652, 39.115427318801096), (506.6666666666667, 39.11542731880104)]


def plot_points(points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.plot(x_values, y_values, marker='o', linestyle='-', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')
    plt.grid(True)
    plt.show()

plot_points(points)
