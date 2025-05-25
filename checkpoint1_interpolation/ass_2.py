import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np

def draw_track():
    # Load the waypoint coordinates
    data = pd.read_csv('loop_track_waypoints.csv')
    data = data.drop(columns='Index')
    coords = data.values

    # Compute cumulative distances as parameter values
    param = np.zeros(len(coords))
    dist = 0.0
    for i in range(len(coords) - 1):
        param[i] = dist
        dx = coords[i + 1][0] - coords[i][0]
        dy = coords[i + 1][1] - coords[i][1]
        dist += np.hypot(dx, dy)
    param[-1] = dist

    # Create cubic splines for x and y coordinates
    interp_x = CubicSpline(param, coords[:, 0])
    interp_y = CubicSpline(param, coords[:, 1])

    # Generate interpolated points
    param_dense = np.linspace(param[0], param[-1], 1000)
    smooth_x = interp_x(param_dense)
    smooth_y = interp_y(param_dense)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(coords[:, 0], coords[:, 1], color='green', label='Waypoints', marker='x')
    plt.plot(smooth_x, smooth_y, color='navy', label='Interpolated Path', linewidth=2)

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Smooth Path Using Cubic Spline')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    draw_track()
