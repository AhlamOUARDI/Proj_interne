import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

np.random.seed(0)


def random_walk(num_steps, max_step=1):
    start_pos = np.array([0, 0, 0])
    a=[np.array([0, 0, 1]),np.array([0, 0, -1]),np.array([0, 1, 0]), np.array([0, -1, 0]),np.array([1, 0, 0]),np.array([-1, 0, 0])]
    walk=[]
    walk.append(start_pos.tolist())
    steps=start_pos.tolist()
    for i in range (num_steps):
        steps += random.choice(a)
        b=steps.tolist()
        walk.append( b)
    return np.array(walk)


def update_lines(num, walks1, lines):
    for line, walk in zip(lines, walks1):
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines


# one random walks
num_steps = 200
walks =  random_walk(num_steps)
'''

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
lines = [ax.plot([], [], [])[0] for _ in walks]
ax.set(xlim3d=(-10, 10), xlabel='X')
ax.set(ylim3d=(-10, 10), ylabel='Y')
ax.set(zlim3d=(-10, 10), zlabel='Z')
#np.cumsum(steps, axis=0)

# RW Animation
ani = animation.FuncAnimation(fig, update_lines, num_steps, fargs=(walks, lines))
'''

ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
z = [walks[i][2] for i in range (num_steps)]
x = [walks[i][0] for i in range (num_steps)]
y = [walks[i][1] for i in range (num_steps)]
walks =  random_walk(num_steps)
ax.plot(x, y, z)
z1 = [walks[i][2] for i in range (num_steps)]
x1 = [walks[i][0] for i in range (num_steps)]
y1 = [walks[i][1] for i in range (num_steps)]
ax.plot(x1, y1, z1)
walks =  random_walk(num_steps)
z = [walks[i][2] for i in range (num_steps)]
x = [walks[i][0] for i in range (num_steps)]
y = [walks[i][1] for i in range (num_steps)]
ax.plot(x, y, z)

plt.show()