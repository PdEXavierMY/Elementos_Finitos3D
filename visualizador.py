import meshio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_vtu(file_path):
    # Leer el archivo VTU
    mesh = meshio.read(file_path)

    # Obtener los nodos y las celdas del archivo VTU
    points = mesh.points
    cells = mesh.cells_dict

    # Crear una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar los puntos
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='o')

    # Dibujar las celdas
    for key in cells:
        if key.startswith('tetra'):
            tetras = cells[key]
            for tetra in tetras:
                tetra_points = points[tetra]
                tetra_points = np.vstack([tetra_points, tetra_points[0]])  # Cerrar el tetraedro
                ax.plot(tetra_points[:, 0], tetra_points[:, 1], tetra_points[:, 2], c='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.title('Visualización de Archivo VTU')
    plt.show()

# Ruta al archivo VTU
file_paths = ['MEF_beam_bulk_1.vtu', 'MEF_beam_bulk_2.vtu', 'MEF_beam_bulk_3.vtu', 'MEF_beam_bulk_4.vtu', 'MEF_beam_bulk_5.vtu', 'MEF_beam_bulk_6.vtu', 'MEF_beam_bulk_7.vtu', 'MEF_beam_bulk_8.vtu', 'MEF_beam_bulk_9.vtu', 'MEF_beam_bulk_10.vtu']

# Visualizar el archivo VTU
for file_path in file_paths:
    visualize_vtu(file_path)
