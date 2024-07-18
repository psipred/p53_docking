from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

points = pandas.read_csv('dd_test2.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = points['confidence'].values
y = points['samples'].values
z = points['inferences'].values


ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('Confidence score')
ax.set_ylabel('Samples per complex')
ax.set_zlabel('Inference number')
plt.show()