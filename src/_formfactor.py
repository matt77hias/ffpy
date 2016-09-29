from sympy import *
from IPython.display import display

init_printing(use_unicode=False, wrap_line=False, no_global=True)

pretty = True
def _display(expression):
    if pretty:
        display(expression)
    else:
        print(expression)
    
'''
----------------------------------------------------
3D
----------------------------------------------------
solid angle
    measure on the (hemi)sphere
    omega = A / r^2 with A on the (hemi)sphere
    [steradians]

example: 
    hemisphere A = 2 * pi * r^2  => omega = 2 * pi
    sphere     A = 4 * pi * r^2  => omega = 4 * pi

differential solid angle
    d_omega = cos(theta_y) * dA_y / (r_xy)^2

----------------------------------------------------
2D
----------------------------------------------------
angle
    measure on the (half)circle
    theta = L / r
    [radians]

example: 
    halfcircle L =     pi * r  => omega =     pi
    circle     L = 2 * pi * r  => omega = 2 * pi
    
differential angle
    d_angle = cos(theta_y) * dL_y / r_xy
'''

#Current version of sympy is buggy
#The following integrals are wrong (already pending Issue)

def ff_NAABB_orthogonal_2D():
    x, y = symbols('x y')
    w, h = symbols('w h', real=True, nonzero=True, positive=True)
    result = Integral((1/sqrt((x**2 + y**2)**3)), (x,0,w), (y,0,h))
    _display(result)
    result = integrate((1/sqrt((x**2 + y**2)**3)), (x,0,w), (y,0,h))
    _display(result)
    
def ff_NAABB_parallel_2D():
    x, y = symbols('x y')
    w, h = symbols('w h', real=True, nonzero=True, positive=True)
    result = Integral((1.0/sqrt(((y-x)**2 + h**2))**3), (x,0,w), (y,0,w))
    _display(result)
    result = integrate((1.0/sqrt(((y-x)**2 + h**2))**3), (x,0,w), (y,0,w))
    _display(result)