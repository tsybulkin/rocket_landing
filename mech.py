from sympy import cos, sin, diff, symbols
from sympy.physics.mechanics import LagrangesMethod, dynamicsymbols


def init_vars(): return dynamicsymbols('x y a')

def La(x,y,a):
	g, m, L, D, W, u1, u2 = symbols('g m L D W u1 u2')
	dx, dy, da = dynamicsymbols('x y a',1)
	
	T = m * L**2 / 6 * da**2 + m / 2 * (dx**2 + dy**2)
	V = m * g * y

	Eq1 = diff( diff(T-V,dx),'t') - diff(T-V,x) - (u1 + u2) * sin(a)
	Eq2 = diff( diff(T-V,dy),'t') - diff(T-V,y) - (u1 + u2) * cos(a)
	Eq3 = diff( diff(T-V,da),'t') - diff(T-V,a) - (u1 - u2) * W

	return (Eq1, Eq2, Eq3)



def run():
	x,y,a = init_vars()
	Eq1,Eq2,Eq3 = La(x,y,a)
	print "Eq1:", Eq1
	print "\nEq2:", Eq2
	print "\nEq3:", Eq3




if __name__ == '__main__':
	run()



