
from plotting import *
from matplotlib.pyplot import *
from numpy import *

#put x and y values into array
xy = [(1,1),(4,1),(4,4),(1,4)]
x = []
y = []

for i in xy:
    x.append(i[0]) 
    y.append(i[1])

xy_array = array((x,y))

#rotation transformation 
def xy_rotate(xy_array, theta):
    """"
    creates a list for transformed plot rotated theta degrees
    """
    try:
        theta_radians = radians(theta)
    except:
        print ('invalid input')
        return None

    R = array(( (cos(theta_radians), -sin(theta_radians) ),
                (sin(theta_radians), cos(theta_radians)) ))

    transformed_xy = list(R@xy_array)
    x_transformed = transformed_xy[0]
    y_transformed = transformed_xy[1]

    list_xy_rotated = list(zip(x_transformed, y_transformed))
    return list_xy_rotated

#shear transformation 
def xy_shear(xy_array, k):
    """"
    creates a list for transformed plot rotated sheared by k
    """
    try:
        k_value = int(k)
    except:
        print ('invalid input')
        return None

    S = array (( (1, k_value),
                (0, 1) ))

    transformed_xy = list(S@xy_array)
    x_transformed = transformed_xy[0]
    y_transformed = transformed_xy[1]

    list_xy_shear = list(zip(x_transformed, y_transformed))
    return list_xy_shear
    
plot_transformation(xy, xy_shear(xy_array, 1.1))
show()

plot_transformation(xy, xy_rotate(xy_array, 45))
show()




