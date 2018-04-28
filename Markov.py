import numpy as np
from matplotlib import pyplot

P = np.matrix([[0.25,0.25,0.50],
                                 [ 0.1,0.3,0.6],
                                 [0.05,0.15,0.80]])

v = np.matrix([[1,0,0],
                                 [0,1,0],
                                 [0,0,1]])

# Get the data
plot_data = []
for step in range(20):
    result = v * P**step
    plot_data.append(np.array(result).flatten())

# Convert the data format
plot_data = np.array(plot_data)

# Create the plot
pyplot.figure(1)
pyplot.xlabel('Steps')
pyplot.ylabel('Probability')
lines = []
for i, shape in zip(range(6), ['x', 'h', 'H', 's', '8', 'r+']):
    line, = pyplot.plot(plot_data[:, i], shape, label="S%i" % (i+1))
    lines.append(line)
pyplot.legend(handles=lines, loc=1)
pyplot.show()
