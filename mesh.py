import pandas as pd
import numpy as np

def create_mesh(x, y, interval):
    mesh_x, mesh_y = [], []
    for j in np.arange(0, y + interval, interval):
        for i in np.arange(0, x + interval, interval):
            mesh_y.append(j)
            mesh_x.append(i)

    mesh = pd.DataFrame({'mesh_x': mesh_x, 'mesh_y': mesh_y})
    mesh.to_csv('whole_mesh.txt', header = None, index = False, sep = ' ')
    return mesh

def create_element(x, y, interval):
    a, b, c, d = [], [], [], []
    vertical_num, horizontal_num = y // interval, x // interval
    for j in range(int(vertical_num)):
        for i in range(int(horizontal_num)):
            a.append(int(j * (horizontal_num + 1) + i))
            b.append(int(j * (horizontal_num + 1) + i + 1))
            c.append(int((j + 1) * (horizontal_num + 1) + i + 1))
            d.append(int((j + 1) * (horizontal_num + 1) + i))
    element = pd.DataFrame({'a': a, 'b': b, 'c': c, 'd': d})
    element.to_csv('element.txt', header = None, index = False, sep = ' ')
    return element

def create_mesh_txt(x, y, interval):
    mesh_length = len(create_mesh(x, y, interval))
    element_length = len(create_element(x, y, interval))

    mesh_file = open('whole_mesh.txt').read()
    element_file = open('element.txt').read()

    mesh_txt = open('mesh.txt', 'w')
    mesh_txt.write(str(mesh_length))
    mesh_txt.write(' ')
    mesh_txt.write(str(element_length))
    mesh_txt.write('\n')

    mesh_txt.write(mesh_file)
    mesh_txt.write('\n')
    mesh_txt.write(element_file)
    mesh_txt.close()

    return None

if __name__ == '__main__':
    create_mesh_txt(10, 10, 1)