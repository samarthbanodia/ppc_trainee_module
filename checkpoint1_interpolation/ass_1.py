import random
import matplotlib.pyplot as plotter
import numpy as np
import pandas as pd



x_array = []
y = []
# file = pd.read_csv('loop_track_waypoints.csv')
# for index,row in file.iterrows():
#     x_array = row['X']
#     y = row['Y']
for _ in range(4):
    x_array.append(random.randint(0, 101))
    y.append(random.randint(0, 101))
    
    
sorted_x = np.sort(np.array(x_array))    
sorted_y = np.sort(np.array(y))  


def interpolation(x_array,y) :
    matrix_array = np.array([[x_array[0]**3 , x_array[0]**2 ,x_array[0], 1 ,0 , 0 , 0 , 0 ,0 , 0 , 0 , 0],
                         [x_array[1]**3 , x_array[1]**2 ,x_array[1], 1 ,0 , 0 , 0 , 0 ,0 , 0 , 0 , 0],
                         [0 , 0 , 0 , 0, x_array[1]**3 , x_array[1]**2 ,x_array[1], 1, 0, 0, 0, 0],
                         [0 , 0 , 0 , 0, x_array[2]**3 , x_array[2]**2 ,x_array[2], 1, 0, 0, 0, 0],
                         [0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , x_array[2]**3 , x_array[2]**2 ,x_array[2], 1],
                         [0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , x_array[3]**3 , x_array[3]**2 ,x_array[3], 1],
                         [3 * x_array[1]**2 , 2 * x_array[1] ,1, 0 ,-3 * x_array[1]**2 , -2 * x_array[1] ,-1, 0 ,0 , 0 , 0 , 0],
                         [0, 0, 0, 0, 3 * x_array[2]**2 , 2 * x_array[2] ,1, 0, -3 * x_array[2]**2 , -2 * x_array[2] ,-1, 0],
                         [6 * x_array[1] , 2, 0, 0, -6 * x_array[1] , -2, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 6 * x_array[2] , 2, 0, 0, -6 * x_array[2] , -2, 0, 0],
                         [3 * x_array[1]**2 , 2 * x_array[1] ,1, 0 ,0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 3 * x_array[1]**2 , 2 * x_array[1] ,1, 0]])

      

    constants = np.array([[y[0]],
                          [y[1]],
                          [y[1]],
                          [y[2]],
                          [y[2]],
                          [y[3]],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0],
                          [0]
                          ])
    
    coefficients = np.linalg.solve(matrix_array, constants)
    return coefficients
    
    
def function_plot(x,a,b,c,d):
    return  a*x**3+b*x**2 + c*x + d   

coeffs = interpolation(sorted_x,sorted_y)

for i in range(0,3):
    x_final = np.linspace(sorted_x[0+i],sorted_x[1+i], 1000)
    y_final = function_plot(x_final,coeffs[i*4],coeffs[i*4 +1],coeffs[i*4 +2],coeffs[i*4 +3])
    plotter.plot(x_final,y_final)

    
# plotter.plot(x ,function_plot(x,coeffs[0],coeffs[1],coeffs[2], coeffs[3]) , color = 'red')
plotter.plot(x_final,y_final)

plotter.scatter(sorted_x, sorted_y , label = "waypoints")
plotter.legend(loc = 'upper left')

plotter.grid(linewidth = 0.1)
plotter.show()