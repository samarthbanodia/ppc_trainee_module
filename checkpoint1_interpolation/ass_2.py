import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def main():
    waypoints = pd.read_csv('loop_track_waypoints.csv')

    waypoints = waypoints.drop('Index', axis=1)
    waypoints = waypoints.to_numpy()
    
    sum = 0
    t = np.zeros(waypoints.shape[0])
    
    for i in range(waypoints.shape[0]-1):
        t[i] = sum
        x_dist = waypoints[i+1][0] - waypoints[i][0]
        y_dist = waypoints[i+1][1] - waypoints[i][1]
        sum += np.sqrt(x_dist**2 + y_dist**2)
    
    t[-1] = sum #last point's parameter value
    
    spline_x = CubicSpline(t, waypoints[:, 0])
    spline_y = CubicSpline(t, waypoints[:, 1])
    
    
    t_cont = np.linspace(t[0], t[-1], 1000) #scale
    x_cont = spline_x(t_cont)
    y_cont = spline_y(t_cont)
    
    plt.figure(figsize=(10, 7))
    
    plt.scatter(waypoints[:, 0], waypoints[:, 1], color='red', label='waypointss')
    
    plt.plot(x_cont, y_cont, color='blue', label='interpolation')
    
    plt.legend()
    plt.grid(True)
    
    plt.axis('equal')
    
    plt.show()
    

if __name__ == "__main__":
    main()