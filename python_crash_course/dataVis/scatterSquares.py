import matplotlib.pyplot as plot

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plot.scatter(x_values, y_values, c=y_values, cmap=plot.cm.Blues, edgecolor='none', s=40)

plot.title("Square Nmbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of value", fontsize=14)
plot.tick_params(axis='both', which='major', labelsize=14)
plot.axis([0, 1100, 0, 1100000])
plot.savefig('scatter_squares.png', bbox_inches='tight')
plot.show()