# TFG NRRHHH: 

Este repositorio recoge los archivos de mi proyecto de fin de carrera.

Proyecto desarrollado por Noelia Regidor Hontana

Universidad Carlos III de Madrid

Año 2025

# VariacionTorquesGraficaRobot:

Permite leer y visualizar en tiempo real los pares articulares externos (exttorque) de un robot colaborativo ABB GoFa, usando comunicación por sockets y gráficos con Matplotlib.

Se compone de dos partes:

1. **Script RAPID (robot):**
   - Abre un servidor TCP en el puerto 1025.
   - Envía continuamente los torques externos de las 6 articulaciones separados por `|`.

2. **Script Python (PC):**
   - Se conecta al robot como cliente TCP.
   - Recibe los datos y actualiza una gráfica en tiempo real para cada articulación.
