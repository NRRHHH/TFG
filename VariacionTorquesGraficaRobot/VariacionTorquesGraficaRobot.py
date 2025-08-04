# Live plotting of external joint torques received via TCP socket from an ABB robot

import collections
import matplotlib.pyplot as plt
import numpy as np
import socket 
import time

# -------------------- Configuration parameters ----------------------- #
STEPS = 100                    # Number of samples to display on the plot
TIME_INTERVAL = 0.001          # Update interval (s)

# -------------------- Initialize connection -------------------------- #
mi_socket = socket.socket() 
mi_socket.connect(("192.168.125.1" , 1025)) 
print(mi_socket.recv(1024)) 

# -------------------- Prepare plot ----------------------------------- #
t = np.arange(0, STEPS)
values = [collections.deque(np.zeros(t.shape)) for i in range(6)]
limits = (0, 0)

fig, axes = plt.subplots(1, 1)
axes.set_title('Torques')
axes.set_ylabel('Nm') 
axes.set_animated(True)
axes.legend(loc='upper right') 

(ln_q1,) = axes.plot(values[0], label='ExtTorque, axis 1', color='red')
(ln_q2,) = axes.plot(values[1], label='ExtTorque, axis 2', color='green')
(ln_q3,) = axes.plot(values[2], label='ExtTorque, axis 3', color='blue')
(ln_q4,) = axes.plot(values[3], label='ExtTorque, axis 4', color='yellow')
(ln_q5,) = axes.plot(values[4], label='ExtTorque, axis 5', color='pink')
(ln_q6,) = axes.plot(values[5], label='ExtTorque, axis 6', color='orange')

plt.show(block=False)
plt.pause(0.1)

bg = fig.canvas.copy_from_bbox(fig.bbox)
fig.draw_artist(axes)
fig.canvas.blit(fig.bbox)

# -------------------- Main loop ------------------------------------- #
while True:
  respuesta = mi_socket.recv(1024).decode('utf-8') 
  arr_str = respuesta.split('|')

  try:
    arr_num = [float(s) for s in arr_str]
    if len(arr_num) != 6: 
        continue  # Skip if not exactly 6 values

    for i in range(len(values)):
      values[i].popleft()
      values[i].append(arr_num[i])
      print(f"Canal {i+1}: Últimos valores -> {list(values[i])[-6:]}")  # Show last 5 values

    fig.canvas.restore_region(bg)

    ln_q1.set_ydata(values[0])
    ln_q2.set_ydata(values[1])
    ln_q3.set_ydata(values[2])
    ln_q4.set_ydata(values[3])
    ln_q5.set_ydata(values[4])
    ln_q6.set_ydata(values[5])

    limits = (min([limits[0]] + arr_num[0:6]), max([limits[1]] + arr_num[0:6]))
    axes.set_ylim(-100, 100)

    fig.draw_artist(axes) 
    fig.draw_artist(ln_q1) 
    fig.draw_artist(ln_q2) 
    fig.draw_artist(ln_q3) 
    fig.draw_artist(ln_q4) 
    fig.draw_artist(ln_q5) 
    fig.draw_artist(ln_q6) 

    fig.canvas.blit(fig.bbox)
    fig.canvas.flush_events()

    time.sleep(TIME_INTERVAL) 

  except Exception as e:
    print("Error in main loop:", e)

mi_socket.sendall('Server connected'.encode()) 
mi_socket.close() 
