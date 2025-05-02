import numpy as np

def stanley_steering(x, y, yaw, v, waypoints, k=1.0, ks=1e-2, max_steer=np.radians(30)):
    """
    Stanley steering controller.

    Args:
        x, y     : rear axle position of the car
        yaw      : vehicle heading angle (in radians)
        v        : vehicle speed
        waypoints: Nx2 array of path waypoints
        k        : cross-track gain
        ks       : softening term to prevent div by zero
        max_steer: steering angle limits (in radians)

    Returns:
        steer       : steering angle in radians
        target_idx  : index of the nearest waypoint
    """
    # Step 1: Compute front axle position
    L = 2.5  # assume fixed wheelbase
    fx = x + L * np.cos(yaw)
    fy = y + L * np.sin(yaw)

    # Step 2: Find nearest waypoint
    x_dist = waypoints[:, 0] - fx
    y_dist = waypoints[:, 1] - fy
    dist = np.sqrt(x_dist**2 , y_dist**2)
    target_idx = np.argmin(dist)


    # Step 3: Compute heading of path at that point
    next_waypoint = waypoints[target_idx+1]
    path_dx = next_waypoint[0] - waypoints[target_idx][0] #getting slope of the path using  2points
    path_dy = next_waypoint[1] - waypoints[target_idx][1]
    path_yaw = np.arctan2(path_dy, path_dx)


    # Step 4: Compute heading error
    heading_error = path_yaw - yaw



    # Step 5: Compute signed cross-track error
    m = np.tan(path_yaw)
    c = waypoints[target_idx][1] - m * waypoints[target_idx][0]
    cross_track_error = abs(m * fx - fy + c) / np.sqrt(m**2 + 1) # perpendiuclar distance from a line formula 


    # Step 6: Compute steering using Stanley law
    steer = heading_error + np.arctan2(k * cross_track_error, v + ks) # write your code here
    steer = np.clip(steer, -max_steer, max_steer)

    return steer, target_idx



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
Kd = 0.0    #derivative constant  # increase this if you want the animation to be longer
pid = PIDController(Kp, Ki, Kd)


def pid_throttle(target_speed, current_speed, dt):
    error = target_speed - current_speed
    return pid.update(error, dt)