import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-sy.sqrt(x)), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[1,1,1,1,1,1,1,1,1,1], [1,2,3,4,5,6,7,8,9,0],[3,4,6,8,11,2,7,10,0,0],[2,1,7,9,1,12,3,0,0,0],[4,3,1,6,7,9,0,0,0,0],[5,6,7,10,11,0,0,0,0,0],[1,1,4,5,0,0,0,0,0,0],[1,10,3,0,0,0,0,0,0,0],[10,11,0,0,0,0,0,0,0,0],[12,0,0,0,0,0,0,0,0,0]] )
    b = np.array([55,285,257,159,126,133,35,30,32,12])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1201431
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
