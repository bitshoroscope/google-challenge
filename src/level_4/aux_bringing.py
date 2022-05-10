from pylab import *
from google import simmetry as sim


def get_sequences(matrix):
    x = []
    y = []
    for i in matrix:
        x.append(i[0])
        y.append(i[1])
    return x, y

def get_soldier_matrix(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power):
    matrix = set()
    x = sim.get_sequence(me_x, soldier_x, wall_x, power)
    y = sim.get_sequence(me_y, soldier_y, wall_y, power)

    for i in x:
        for j in y:
            coord = (i,j)
            matrix.add(coord)

    return matrix

xmin, xmax, ymin, ymax = -25,25,-25,25
ticks_frequency = 1

fig, ax = plt.subplots(figsize=(10,10))
fig.patch.set_facecolor('#ffffff')

ax.set(xlim=(xmin-1,xmax+1), ylim=(ymin-1,ymax+1), aspect='equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
ax.set_xlabel('$y$', size=14, labelpad=-24, x=1.02, rotation=0)

plt.text(0.49, 0.49, r"$0$", ha='right', va='top', transform=ax.transAxes, horizontalalignment='center', fontsize=14)

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

input = ([2,5], [1,2], [1,4], 15)
walls = input[0]
me = input[1]
soldier = input[2]
power = input[3]

wall_x = walls[0]
wall_y = walls[1]
me_x = me[0]
me_y = me[1]
soldier_x=soldier[0]
soldier_y=soldier[1]

soldiers_orig = get_soldier_matrix(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)
mes_orig = get_soldier_matrix(wall_x, wall_y, me_x, me_y, me_x, me_y, power)

soldiers = sim.generate_matrix(wall_x, wall_y, me_x, me_y, soldier_x, soldier_y, power)
mes = sim.generate_matrix(wall_x, wall_y, me_x, me_y, me_x, me_y, power)

vertices = sim.get_vertex_matrix_yield(wall_x,wall_y,me_x,me_y, power)

mes_orig_x, mes_orig_y = get_sequences(mes_orig)
soldiers_orig_x, soldiers_orig_y = get_sequences(soldiers_orig)
mes_x, mes_y = get_sequences(mes)
soldiers_x, soldiers_y = get_sequences(soldiers)
vertex_x, vertex_y = get_sequences(vertices)

soldiers_sol_x = [3, -1, 3, -1, 5, -3, -5, 3, -1, 7, 7, -3, 5, -5, -7, 9, -1, 3, 7, -5, 7, 9, -7, -5, 11, -9, -9, 11, -9, 11, 13, 3, -1, -11, -9, 11, -1, 3, 15, -13, -13, -3, 5, 15]
soldiers_sol_y = [4, 4, 6, 6, 4, 4, 4, -4, -4, 4, 6, -4, -4, 6, 4, 4, -6, -6, -4, -4, -6, -4, -4, -6, 4, 4, 6, 6, -4, -4, 4, 14, 14, 4, -6, -6, 16, 16, 4, 4, 6, 16, 16, 6]
scatter(soldiers_sol_x,soldiers_sol_y, s=100 ,marker='x', c='b')

scatter(soldiers_x,soldiers_y, s=100 ,marker='o', c='k')
scatter(mes_x, mes_y, s=100 ,marker='o', c='g')

scatter(soldiers_orig_x,soldiers_orig_y, s=100 ,marker='o', c='b', alpha=.5)
scatter(mes_orig_x, mes_orig_y, s=100 ,marker='o', c='g', alpha=.5)

scatter(vertex_x, vertex_y, s=100 ,marker='o', c='r')

# Grafica me to soldiers
for i,j in zip(soldiers_x,soldiers_y):
    x_values = [me_x,i]
    y_values = [me_y,j]
    plt.plot(x_values, y_values, color="red", alpha=.5)

for i in range (-wall_x*5, wall_x*5, wall_x):
    x_values = [i,i]
    y_values = [-15,15]
    plt.plot(x_values, y_values, color="black", alpha=0.8)

for i in range (-wall_y*10, wall_y*10, wall_y):
    x_values = [-15,15]
    y_values = [i,i]
    plt.plot(x_values, y_values, color="black", alpha=0.8)




cc = plt.Circle((me_x, me_y), power, alpha=0.3)

ax.set_aspect(1)
ax.add_artist(cc)
plt.show()


plt.show()
