from solver import Solver
from pytest import approx
import numpy as np

def test_solver_init():
    solver = Solver(
        n=3,
        x=[[2, 6], [7, 8], [-2, 5]],
        u=[[0.5, 0.1], [10, 2], [-1, 4]],
        types=[0, 0, 1],
        delta_t=0.2,
    )
    assert solver.x == [[2, 6], [7, 8], [-2, 5]]
    assert solver.u == [[0.5, 0.1], [10, 2], [-1, 4]]
    assert solver.types == [0, 0, 1]
    assert solver.delta_t == 0.2

def test_calc_f():
    ''''
    Unit test for the function calculating the propulsion F
    '''
    
    # Set parameters to some chosen values
    n = 100
    x = 3*np.ones([n, 2])
    u = 2*np.ones([n, 2])
    vd = np.ones([n, 2])
    types = np.ones([n, 1])
    delta_t = 1 
    
    a = Solver(n, x, u, types, delta_t)
    solver_solution = a._Solver__calc_f(vd)
    correct_solution = (vd-u)/a._tau
    
    # Check if the solver solution and the correct_solution are approximately equal
    assert approx(solver_solution) == correct_solution

def test_types_and_vd_consistency():
    '''
    Unit test if type of person (0 or 1) is consistend with desired velocity (vd)
    '''
    n = 10
    x = 3*np.ones([n, 2])
    u = 2*np.ones([n, 2])
    types = np.random.choice(2,n)
    delta_t = 1 

    solver = Solver(n, x, u, types, delta_t)
    vd = solver._Solver__calc_vdterm()

    vd_right = vd[:,0][types==0]
    vd_left = vd[:,0][types==1]

    '''
    type 0 should have positive u-component for vd, 
    type 1 should have negative u-component for vd.
    '''
    assert all(i>0 for i in vd_right)
    assert all(i<0 for i in vd_left)