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
file_path = 'MEF_beam_bulk_1.vtu'

# Visualizar el archivo VTU
visualize_vtu(file_path)
