import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

class Drone:
    def __init__(self):
        self.height = 0.0
        self.velocity = 0.0

    def update(self, thrust, dt):
        gravity = -9.81    
        mass = 1.0
        acceleration = (thrust / mass) + gravity
        self.velocity += acceleration * dt
        self.height += self.velocity * dt
        return self.height

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        # you might need to add more variables here... hint: for Integral controller
        self.sum_integral =0 #to sum(integrate) the error*dt term over and over again
        self.last_error  = 0# to get the d(e(t)) that is the change in errror

    def update(self, error, dt):
        '''
        write the update function on your own
        input is error and dt
        output should be the thrust that is provided to drone
        '''
        self.sum_integral += error*dt
        output = self.Kp*error + self.Ki *self.sum_integral + self.Kd * ((error - self.last_error)/dt)
        self.last_error = error
        return output
        
'''
Start with a P controller, then PD, then PI, and then PID, by trial and error
Your aim here is to tune the controller such that there is minimal overshoot and oscillations
'''
Kp = 1.0    #proportional constant
Ki = 0.0    #integral constant
Kd = 0.0    #derivative constant

target_height = 10.0    # target height of drone
sim_time = 10    # increase this if you want the animation to be longer
dt = 0.05
steps = int(sim_time / dt)
drone = Drone()
pid = PIDController(Kp, Ki, Kd)

heights = []
times = []

for i in range(steps):
    t = i * dt

    error = target_height - drone.height # What should be the error?

    thrust = pid.update(error, dt)
    h = drone.update(thrust, dt)
    times.append(t)
    heights.append(h)
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 15)   # increase the 2nd argument of ylim if you wanna see further above the setpoint
ax.set_xlabel("Drone")
ax.set_ylabel("Height (m)")
ax.set_title("Drone Height Stabilization (PID Control)")

drone_body, = ax.plot([], [], 'bo', markersize=15)
target_line = ax.axhline(y=target_height, color='r', linestyle='--', label='Target Height')
ax.legend()

def init():
    drone_body.set_data([], [])
    return drone_body,

def update(frame):
    x = 0
    y = heights[frame]
    drone_body.set_data([x], [y])
    return drone_body,

ani = animation.FuncAnimation(
    fig, update, frames=len(heights), init_func=init,
    interval=dt*800, blit=True
)

plt.close(fig)
HTML(ani.to_jshtml())
