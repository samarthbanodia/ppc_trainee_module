import random
import matplotlib.pyplot as plt
import numpy as np

def interpolation(x_array, y, start, end):

    # Extract boundary condition values
    d2_start = start
    d2_end = end
    
    # Build the system of equations matrix
    matrix_array = np.array([
        [x_array[0]**3, x_array[0]**2, x_array[0], 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [x_array[1]**3, x_array[1]**2, x_array[1], 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, x_array[1]**3, x_array[1]**2, x_array[1], 1, 0, 0, 0, 0],
        [0, 0, 0, 0, x_array[2]**3, x_array[2]**2, x_array[2], 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, x_array[2]**3, x_array[2]**2, x_array[2], 1],
        [0, 0, 0, 0, 0, 0, 0, 0, x_array[3]**3, x_array[3]**2, x_array[3], 1],
        [3*x_array[1]**2, 2*x_array[1], 1, 0, -3*x_array[1]**2, -2*x_array[1], -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3*x_array[2]**2, 2*x_array[2], 1, 0, -3*x_array[2]**2, -2*x_array[2], -1, 0],
        [6*x_array[1], 2, 0, 0, -6*x_array[1], -2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6*x_array[2], 2, 0, 0, -6*x_array[2], -2, 0, 0],
        [6*x_array[0], 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Second derivative at first point
        [0, 0, 0, 0, 0, 0, 0, 0, 6*x_array[3], 2, 0, 0]   # Second derivative at last point
    ])
    
    # Build the right-hand side constants vector
    constants = np.array([
        y[0], y[1], y[1], y[2], y[2], y[3],
        0, 0, 0, 0, d2_start, d2_end  # Last two values are second derivatives at endpoints
    ])
    
    # Solve system of equations
    coefficients = np.linalg.solve(matrix_array, constants)
    
    return coefficients

def function_plot(x, a, b, c, d):
    """Evaluate cubic polynomial at point x."""
    return a*x**3 + b*x**2 + c*x + d

def calculate_curvature_at_point(x, coeffs, segment_index):
    """
    Calculate curvature at point x using the formula:
    κ(x) = |y''(x)| / (1 + (y'(x))^2)^(3/2)
    
    For planar curves, this is the proper curvature formula when x is the parameter.
    """
    # Get coefficients for this segment
    a = coeffs[segment_index*4]
    b = coeffs[segment_index*4 + 1]
    c = coeffs[segment_index*4 + 2]
    
    # First and second derivatives
    first_derivative = 3*a*x**2 + 2*b*x + c
    second_derivative = 6*a*x + 2*b
    
    # Calculate curvature
    numerator = abs(second_derivative)
    denominator = (1 + first_derivative**2)**(3/2)
    
    # # Avoid division by zero
    # if denominator < 1e-10:
    #     return 0
    
    return numerator / denominator

def calculate_waypoint_curvatures(x_array, coeffs):
    curvatures = []
    curvatures.append(calculate_curvature_at_point(x_array[0], coeffs, 0))
    
    curvature_seg0 = calculate_curvature_at_point(x_array[1], coeffs, 0)
    curvature_seg1 = calculate_curvature_at_point(x_array[1], coeffs, 1)
    curvatures.append((curvature_seg0 + curvature_seg1) / 2)
    
    curvature_seg1 = calculate_curvature_at_point(x_array[2], coeffs, 1)
    curvature_seg2 = calculate_curvature_at_point(x_array[2], coeffs, 2) #take avg of both segments
    curvatures.append((curvature_seg1 + curvature_seg2) / 2)
    
    curvatures.append(calculate_curvature_at_point(x_array[3], coeffs, 2))  
    
    return curvatures

def calculate_total_curvature(x_array, coeffs, num_points=100):
    """Calculate total squared curvature along the spline (cost function)."""
    total = 0
    
    # For each segment of the spline
    for i in range(3):
        # Sample points along this segment
        x_samples = np.linspace(x_array[i], x_array[i+1], num_points)
        
        # Calculate curvature at each sample point
        for x in x_samples:
            k = calculate_curvature_at_point(x, coeffs, i)
            total += k**2
    
    return total

def find_optimal_boundary_conditions(x_array, y_array, d2_min=-10, d2_max=10, num_steps=20):
    """
    Find optimal second derivative boundary conditions that minimize curvature.
    Uses a grid search approach.
    """
    # Values to try for second derivatives at endpoints
    d2_values = np.linspace(d2_min, d2_max, num_steps)
    
    min_cost = float('inf')
    optimal_bc = None
    optimal_coeffs = None
    
    # Try all combinations of boundary conditions
    for d2_start in d2_values:
        for d2_end in d2_values:
            
  
            coeffs = interpolation(x_array, y_array, d2_start, d2_end)
                
            cost = calculate_total_curvature(x_array, coeffs)
                
            if cost < min_cost:
                min_cost = cost
                optimal_start = d2_start
                optimal_end = d2_end
                optimal_coeffs = coeffs
  
    
    return optimal_start , optimal_end, optimal_coeffs, min_cost

def main():
    # Generate or load waypoints
    x_array = []
    y_array = []
    for _ in range(4):
        x_array.append(random.randint(0, 101))
        y_array.append(random.randint(0, 101))
    
    # Sort points by x-coordinate
    indices = np.argsort(np.array(x_array))
    x_sorted = np.array([x_array[i] for i in indices])
    y_sorted = np.array([y_array[i] for i in indices])
    
    # Natural spline (d2=0 at endpoints)
    natural_coeffs = interpolation(x_sorted, y_sorted, 0,0)
    natural_curvatures = calculate_waypoint_curvatures(x_sorted, natural_coeffs)
    natural_total_curvature = calculate_total_curvature(x_sorted, natural_coeffs)
    
    # Find optimal boundary conditions
    optimal_start, optimal_end, optimal_coeffs, optimal_cost = find_optimal_boundary_conditions(x_sorted, y_sorted)
    optimal_curvatures = calculate_waypoint_curvatures(x_sorted, optimal_coeffs)
    
    # plt.figure(figsize=(10, 6))
    
    # Plot each segment
    for i in range(3):
        x_plot = np.linspace(x_sorted[i], x_sorted[i+1], 1000)
        
        # Natural spline
        a, b, c, d = natural_coeffs[i*4], natural_coeffs[i*4+1], natural_coeffs[i*4+2], natural_coeffs[i*4+3]
        y_natural = function_plot(x_plot, a, b, c, d)
        plt.plot(x_plot, y_natural, 'b-')
        
        a, b, c, d = optimal_coeffs[i*4], optimal_coeffs[i*4+1], optimal_coeffs[i*4+2], optimal_coeffs[i*4+3]
        y_optimal = function_plot(x_plot, a, b, c, d)
        plt.plot(x_plot, y_optimal, 'g-')
    
    # Plot waypoints
    plt.scatter(x_sorted, y_sorted, color='red', s=50, label='Waypoints')
    
    # Add legend
    plt.plot([], [], 'b-', label='without opt')
    plt.plot([], [], 'g-', label='optimized ')
    
    plt.grid(linewidth=0.1)
    plt.legend(loc='best')  
    plt.show()

if __name__ == "__main__":
    main()
