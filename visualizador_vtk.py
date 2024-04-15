import vtk

def visualize_vtu(file_path):
    # Crear un lector para el archivo VTU
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(file_path)
    reader.Update()

    # Crear un mapper
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Crear un actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Crear un renderizador y agregar el actor
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)

    # Crear una ventana de renderizado y agregar el renderizador
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)

    # Crear un interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Establecer el estilo de interacción
    style = vtk.vtkInteractorStyleTrackballCamera()
    interactor.SetInteractorStyle(style)

    # Configurar la cámara para que se centre en los datos
    renderer.ResetCamera()

    # Iniciar la interacción
    interactor.Initialize()
    interactor.Start()

# Ruta al archivo VTU
file_path = 'MEF_beam_bulk_10.vtu'

# Visualizar el archivo VTU
visualize_vtu(file_path)

# Ruta al archivo VTU
file_path = 'viga.vtu'

# Visualizar el archivo VTU
visualize_vtu(file_path)
