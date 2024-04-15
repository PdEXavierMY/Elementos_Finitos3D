# Elementos_Finitos3D

Pincha [aquí](https://github.com/PdEXavierMY/Elementos_Finitos3D/) para dirigirte a mi repositorio.

En este repositorio se encuentra el código solución al siguiente problema:

En el umbral de una nueva era de ingeniería digital, la Universidad Alfonso X "El Sabio" se enorgullece de presentar un desafío intelectual único en el campo de la Inteligencia Artificial aplicada al Método de Elementos Finitos (MEF) 3D. 

Este examen no solo evaluará su comprensión técnica de los principios fundamentales del MEF y la programación en Python, sino que también pondrá a prueba su capacidad para integrar estos conocimientos en soluciones creativas y eficientes para problemas estructurales complejos. 

A través de este examen, se espera que los estudiantes demuestren no solo su habilidad técnica, sino también su capacidad innovadora en la simulación y análisis de estructuras utilizando herramientas computacionales avanzadas. Esta evaluación es un paso crucial en su camino para convertirse en pioneros de la ingeniería del futuro.

Instrucciones: Resuelva los siguientes problemas utilizando Python. Asegúrese de documentar su código adecuadamente y de seguir los estándares de codificación discutidos en clase. Es fundamental que su código sea legible y esté bien organizado.

Tiempo: 2 horas

Parte I: Fundamentos de Elementos Finitos

Introducción a Python

Escriba un script en Python que genere y muestre un arreglo tridimensional representando un dominio estructural simple. Asegúrese de comentar cada parte del código para explicar su funcionamiento.

Introducción a Paraview

Desarrolle un script en Python que exporte los resultados de un análisis estructural (presiones y desplazamientos) a un formato compatible con Paraview. Explique cómo visualizar estos resultados en Paraview.

Funciones Auxiliares en Python

Implemente una función en Python que calcule el tensor de deformaciones para un elemento finito tetraédrico dada su matriz de desplazamientos nodales.

Parte II: Pre-procesamiento y Análisis 4. Pre-procesado de Datos

Escriba un script para generar un mallado de tetraedros a partir de una geometría básica proporcionada. Detalle el proceso de mallado y los criterios usados para la generación de elementos.

Implementación de Función de Forma

Implemente la función de forma de un elemento tetraédrico en Python. Verifique su implementación calculando la función de forma en puntos seleccionados del dominio.

Ensamblaje de Matrices

Programe el ensamblaje de la matriz de rigidez global para una estructura mallada con tetraedros. Asegúrese de implementar condiciones de contorno apropiadas y de verificar la simetría de la matriz resultante.

Parte III: Solución y Post-procesamiento 7. Solución de Sistema de Ecuaciones

Desarrolle un solver para el sistema de ecuaciones resultante del método de elementos finitos. Discuta la selección del método numérico y su impacto en la eficiencia y precisión de la solución.

Post-procesamiento

Genere un script para calcular y visualizar las tensiones y deformaciones en la estructura analizada. Integre su código con Paraview para la visualización de los resultados.

Caso de Estudio

Aplique todo el flujo de trabajo en un caso de estudio estructural proporcionado. Discuta los resultados y cómo las decisiones tomadas en cada etapa afectaron el resultado final.


El código a ejecutar se encuentra en 0_main_mesh_nodes.py y en 0_main_fem.py dentro de la carpeta Ejemplo_código. Estos py crean los archivos vtu necesarios para visualizar en Paraview. Tras conseguir las matrices de puntos las podemos visualizar con visualizador.py, y para ver la forma que se obtiene al realizar este método solo se debe ejecutar visualizador_vtk.py.

Aquí se muestran distintas vistas del mismo resultado obtenidas por código o gracias a la interfaz Paraview:








