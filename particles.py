import pandas as pd
import numpy as np

def create_particles(x_start, x_end, y_start, y_end, element_size, num):
    particle_x, particle_y = [], []
    initial_dist = element_size / (2 * num)
    particle_interval = 2 * initial_dist
    for j in np.arange(y_start + initial_dist, y_end, particle_interval):
        for i in np.arange(x_start + initial_dist, x_end, particle_interval):
            particle_x.append(i)
            particle_y.append(j)

    particles = pd.DataFrame({'x': particle_x, 'y': particle_y})
    particles.to_csv('particles_temp.txt', index = False, header = None, sep = ' ')
    return len(particles)

def make_particles_txt(x_start, x_end, y_start, y_end, element_size, num):
    particle_length = create_particles(x_start, x_end, y_start, y_end, element_size, num)
    fw = open('particles.txt', 'w')
    target = open('particles_temp.txt').read()
    fw.write(str(particle_length))
    fw.write('\n')
    fw.write(target)
    fw.close()

    return None
