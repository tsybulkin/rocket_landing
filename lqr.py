import numpy as np
import scipy.linalg
from constants import *
 
def lqr(A,B,Q,R):
    """Solve the continuous time lqr controller.
     
    dx/dt = A x + B u
     
    cost = integral x.T*Q*x + u.T*R*u
    """
    X = np.matrix(scipy.linalg.solve_continuous_are(A, B, Q, R))
     
    K = np.matrix(scipy.linalg.inv(R)*(B.T*X))
     
    eigVals, eigVecs = scipy.linalg.eig(A-B*K)
     
    return K, eigVals



if __name__ == '__main__':
    
    C = 3*W/m/(L**2)

    A = np.array([[0., 1., 0., 0.],
                  [0., 0., -G-V0**2/2/Y0, 0.],
                  [0., 0., 0., 1.],
                  [0., 0., 0., 0.]
                  ]) 
    
    B = np.array([[0.],
                  [0.],
                  [0.],
                  [C]])
    
    Q = np.eye(4) * np.array([1/10., 10., 10., 10.])
    R = np.eye(1) * 1.e-8

    K, eigenvals = lqr(A,B,Q,R)
    print "K:",K,"\neigen vals:",eigenvals
    