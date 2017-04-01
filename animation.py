# This module contains animation of rocket landing
#
#

from constants import L,W
from math import sin, cos


SVG_DIM = 1100, 650
XY0 = SVG_DIM[0]/2, SVG_DIM[1]-5
scale = 3.3 # 3 pixels per meter
Umax = 1.4e6  # 1.0 MegaN

	
def show_animation(log):
	N = len(log)
	[Ti, X,Y,A,U] = zip(*log[-N:])

	f = open('landing.html','w')
	f.write("<html>\n<body background='desert2.png'>\n<svg width='%i' height='%i'>\n" % SVG_DIM)

	f.write("<text x='30' y='80' font-family='Verdana' font-size='48' fill='white'>\
    	Rocket landing  </text>")

	# draw ground
	f.write("<line x1='%i' y1='%i' x2='%i' y2='%i' \
		style='stroke:rgb(80,80,80);stroke-width:3'/>\n" %( x_to_px(-5.), y_to_px(0.), 
													x_to_px(5.), y_to_px(0.) ))
		
	draw_rocket(Ti,X,Y,A,U,f)

	f.write("</svg>\n</body>\n</html>")
	f.close()


def draw_rocket(Ti,X,Y,A,U,f):
	color = 'rgb(230, 230, 210)'
	w = scale * 2 * W * 1.5

	start, dur = Ti[0], Ti[1] - Ti[0]
	
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
		f.write("\t\t<set attributeName='x1' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' fill='freeze' />\n" %(x1,t-start,dur) ),
		f.write("\t\t<set attributeName='y1' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' fill='freeze' />\n" %(y1,t-start,dur) ),
		f.write("\t\t<set attributeName='x2' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' fill='freeze'/>\n" %(x2,t-start,dur) ),
		f.write("\t\t<set attributeName='y2' attributeType='XML'\n \
         to='%i' begin='%.3fs' dur='%.3fs' fill='freeze'/>\n" %(y2,t-start,dur) )
	
	f.write("\t</line>\n")	
		
	## flame
	f.write("\t<polyline points='0,0 0,0 0,0 0,0 0,0' \
  		style='fill:yellow;stroke:orange;stroke-width:2' >\n")

	for t,x,y,a,u in zip(Ti,X,Y,A,U):
		Z1 = int( (Umax-u)/Umax * L * 2 )
		Z2 = int( (Umax+u)/Umax * L * 2 )
		x1,y1 = x_to_px(x+L*a-1.4*W), y_to_px(y-L+1.4*W*a)
		x2,y2 = x_to_px(x+Z1*a-0.5*W), y_to_px(y-Z1+0.5*W*a)
		x3,y3 = x_to_px(x+L*a), y_to_px(y-L)
		x4,y4 = x_to_px(x+Z2*a+0.5*W), y_to_px(y-Z2-0.5*W*a)
		x5,y5 = x_to_px(x+L*a+1.4*W), y_to_px(y-L-1.4*W*a)
		points = "%i,%i %i,%i %i,%i %i,%i %i,%i" %(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)

		f.write("\t\t<set attributeName='points' attributeType='XML'\n \
         to='%s' begin='%.3fs' dur='%.3fs' />\n" %(points,t-start,dur) ),
	
	f.write("\t</polyline>\n")		

	
def x_to_px(x):
	return int(round(x*scale + XY0[0]))


def y_to_px(y):
	return int(round(XY0[1] - y*scale))




