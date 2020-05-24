from entity_sets import *
from mesh import *
from mpm import *
from particles import *
import numpy as np

def create_whole_files(x_start, x_end, y_start, y_end, particle_num):
    assert particle_num in [2, 4, 5], 'Please choose particle number in 2, 4, 5'

    # 确定元素边长
    length = x_end - x_start
    height = y_end - y_start
    dominant_length = min(length, height)
    element_size = max([round(x, 2) for x in np.arange(0.05 * dominant_length, 0.1 * dominant_length + 0.01, 0.01)
                        if length % round(x, 2) == 0 and height % round(x, 2) == 0])

    # 生成mesh.txt
    create_mesh_txt(max(100, 5 * dominant_length), y_end + 20, element_size)

    # 生成particles.txt
    make_particles_txt(x_start, x_end, y_start, y_end, element_size, particle_num)

    # 生成entity_sets.json
    whole_mesh_x = max(100, 5 * dominant_length)
    mesh_df = create_mesh(whole_mesh_x, y_end + 20, element_size)
    id_0 = list(mesh_df[mesh_df['mesh_x'] == 0].index) + list(mesh_df[mesh_df['mesh_x'] == whole_mesh_x].index)
    id_1 = list(mesh_df[mesh_df['mesh_y'] == 0].index)
    set_entity_sets(id_0, id_1)

    # 生成mpm.json
    set_mpm_characteristics()

if __name__ == '__main__':
    create_whole_files(0, 10, 0, 10, 2)
