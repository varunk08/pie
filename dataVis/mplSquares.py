import matplotlib.pyplot as plot

input_vals = []
squares = []
for n in range(5):
    input_vals.append(n)
    print(n)
    squares.append(n * n)

plot.plot(input_vals, squares, linewidth=5)
plot.title("Square numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of Value", fontsize=14)
plot.tick_params(axis='both', labelsize=14)
plot.show()