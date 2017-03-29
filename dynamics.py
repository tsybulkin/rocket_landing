#
# rocket landing
#
# d2x/dt2 = U/m * a
# d2y/dt2 = U/m - G
# d2a/dt2 = 3*W/m/L^2 * dU

from matplotlib import pyplot as plt
import numpy as np
import sys
from constants import *

	

def control(x,dx,a,da):
	K = np.array([316., 7629., 1.70e6, 9.62e6])
	z = np.array([x,dx,a,da])
	du = - K.dot(z)
	return lim(U0, du)


def run(T=1):
	t = 0

	x, dx = np.random.uniform(-100., 100.), np.random.uniform(-50., 50.) 
	y, dy = Y0, -V0
	a, da = np.random.uniform(-0.1, 0.1), 0.

	print "initial x:%.0f, y:%.0f, a:%.2f" %(x,y,a)
	print "engine thrust: %.1f kN" % (U0/1000.)

	log = []
	
	while t < T:
		du = control(x,dx,a,da)
		x,dx,y,dy,a,da = dynamics(x,dx,y,dy,a,da,du,U0,TAU) 
		log.append((t,x,y,a,du))
		t += TAU
		if y < L:
			break
	check_landing(x,dx,y,dy,a,da)
	show(log)
	

def show(log):
	N = int(len(log)/6)
	[Ti, X,Y,A,U] = zip(*log[-N:])
	plt.figure(1)
	plt.title('simulation results')
	
	plt.subplot(311)
	plt.ylabel('y')
	plt.plot(Ti, Y, 'g-')
	plt.grid(True)
	
	plt.subplot(312)
	plt.ylabel('x')
	plt.plot(Ti, X, 'b-')
	plt.grid(True)
	
	plt.subplot(313)
	plt.ylabel('a')
	plt.plot(Ti, A, 'r-')
	plt.grid(True)
	
	plt.show()


def check_landing(x,dx,y,dy,a,da):
	if abs(dy) > 1.: print "LANDING FAILED"
	if abs(da) > 0.05: print "LANDING FAILED"
	if abs(dx) > 0.05: print "LANDING FAILED"
	print "final x:%.0f, y:%.0f, a:%.2f" %(x,y,a)
	print "final velocity: %.1f" % np.sqrt(dx**2 + dy**2)
	

def lim(LIM, val):
	if val < - LIM: return -LIM
	elif val > LIM: return LIM
	return val


def dynamics(x,dx,y,dy,a,da,du,U,tau):
	dx += U/m * a * tau
	x += dx * tau

	dy += (U/m - G) * tau
	y += dy * tau

	da += (3*W/m/L**2) * du * tau
	a += da * tau
	
	return x,dx,y,dy, a, da


if __name__ == '__main__':
	args = sys.argv[:]
	if len(args) == 2:
		run(float(args[1]))
	else:
		run()

