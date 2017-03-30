# This module contains animation of rocket landing
#
#

from constants import L,W
from math import sin, cos


SVG_DIM = 1100, 650
XY0 = SVG_DIM[0]/2, SVG_DIM[1]-10
scale = 3.3 # 3 pixels per meter

	
def show_animation(log):
	N = len(log)
	[Ti, X,Y,A,U] = zip(*log[-N:])

	f = open('landing.html','w')
	f.write("<html>\n<body>\n<svg width='%i' height='%i'>\n" % SVG_DIM)

	# draw ground
	f.write("<line x1='%i' y1='%i' x2='%i' y2='%i' \
		style='stroke:grey;stroke-width:3'/>\n" %(x_to_px(-50.), y_to_px(0.), 
													x_to_px(50.), y_to_px(0.)) )
	
	f.write("<line x1='%i' y1='%i' x2='%i' y2='%i' \
		style='stroke:blue;stroke-width:3'/>\n" %( x_to_px(-5.), y_to_px(0.), 
													x_to_px(5.), y_to_px(0.) ))
		

	draw_rocket(Ti,X,Y,A,f)

	f.write("</svg>\n</body>\n</html>")
	f.close()


def draw_rocket(Ti,X,Y,A,f):
	color = 'rgb(50, 50, 100)'
	w = scale * 2 * W

	start, dur = Ti[0], Ti[1] - Ti[0]
	#print "rocket width: %i px" % w

	f.write("\t<line x1='%i' y1='%i' x2='%i' y2='%i' \
		style='stroke:%s;stroke-width:%i' >\n" % (0,0,0,0,color,w))
	
	for t,x,y,a in zip(Ti,X,Y,A):
		x1,y1 = x_to_px(x-L*sin(a)), y_to_px(y+L*cos(a))
		x2,y2 = x_to_px(x+L*sin(a)), y_to_px(y-L*cos(a))
		f.write("\t\t<set attributeName='x1' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' />\n" %(x1,t-start,dur) ),
		f.write("\t\t<set attributeName='y1' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' />\n" %(y1,t-start,dur) ),
		f.write("\t\t<set attributeName='x2' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' />\n" %(x2,t-start,dur) ),
		f.write("\t\t<set attributeName='y2' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' />\n" %(y2,t-start,dur) )
	else:
		f.write("\t\t<set attributeName='freeze' attributeType='XML'\n \
         to='True' />\n")
	
	f.write("\t</line>\n")	
	
	

	
def x_to_px(x):
	return int(round(x*scale + XY0[0]))


def y_to_px(y):
	return int(round(XY0[1] - y*scale))




