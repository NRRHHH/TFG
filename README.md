# TFG NRRHHH: 

Este repositorio recoge los archivos de mi proyecto de fin de carrera.

- Proyecto desarrollado por **Noelia Regidor Hontana**  
- Universidad Carlos III de Madrid  
- Año: 2025

# CorrecionTrayectoriaEGM

Agrupa los tres componentes principales del sistema que ejecuta y corrige trayectorias en tiempo real en un robot ABB (GoFa), utilizando EGM y sensores:

1. **RAPID - main trajectory (MainModule):**
   - Utiliza EGMSetupUC y EGMMoveL para mover el robot a través de cuatro puntos (Target_10 → Target_20 → Target_30 → Target_40) formando un rectángulo.
   - Correcciones en tiempo real sobre el eje Z se activan en cada segmento a través de Path Correction.

2. **RAPID – Task 2: Sensor socket server (Module2):**
   - Abre un servidor TCP que lee posición, velocidad y torque de cada articulación (usando GetJointData), y envía los datos por socket.
   - Tiene opción de simulación de valores si no utiliza el robot real.

3. **Python – controlador principal:**
    - Hilo de lectura (sensor_reader) que recibe datos por socket y calcula la fuerza estimada en Z (F_z) usando PyKDL.
    - Inicializa el nodo EGM (EGM()), recibe datos del robot y aplica correcciones en Z mediante send_to_robot_path_corr.
    - Visualiza F_z en una gráfica en tiempo real utilizando Matplotlib.

# VariacionTorquesGraficaRobot

Permite leer y visualizar en tiempo real los pares articulares externos (**exttorque**) de un robot colaborativo ABB GoFa, usando comunicación por sockets y gráficos con Matplotlib.

Se compone de dos partes:

1. **Script RAPID (robot):**
   - Abre un servidor TCP en el puerto 1025.
   - Envía continuamente los torques externos de las 6 articulaciones separados por `|`.

2. **Script Python (PC):**
   - Se conecta al robot como cliente TCP.
   - Recibe los datos y actualiza una gráfica en tiempo real para cada articulación.

# DibujarEspiral.modx

Este módulo permite que el robot trace una trayectoria en espiral en el plano XY, con una herramienta definida y un objeto de trabajo referenciado.

Características:

- Usa instrucciones MoveL para formar una espiral creciente alrededor de un punto central.
- No incorpora control de fuerza.
- Útil como demostración geométrica o base para experimentos de contacto.
