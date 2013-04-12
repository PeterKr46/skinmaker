# standardBrush
import os,sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
	
from brush_class import Brush
from math import sqrt

class airBrush(Brush):
	displayName	= "Airbrush";
	description	= "A very soft Airbrush.";
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "BRUSH";
		this.displayName= "Airbrush"
		this.description= "A very sof Airbrush."
		
	def leaveStamp(this, x, y):
		if( not this.canvas.fits(x,y) ): return False;
		brushsize		= this.canvas.getBrushSize();
		if( this.setColor == False):
			color		= this.canvas.getColor();
		else:
			color 		= this.color;
		
		leftboundary 	= x - brushsize;
		rightboundary 	= x + brushsize + 1;
		topboundary		= y - brushsize;
		bottomboundary	= y + brushsize + 1;
		
		if( leftboundary 	< 0		): leftboundary 	= 0;
		if( rightboundary 	> 64	): rightboundary 	= 64;
		if( topboundary 	< 0 	): topboundary 		= 0;
		if( bottomboundary 	> 32	): bottomboundary 	= 32;
		
		center_x,center_y = x,y;
		center_coords = (x,y);
		
		for x in range(leftboundary,rightboundary):
			for y in range(topboundary,bottomboundary):
				if( not this.canvas.fits(x,y) ): continue;
				coords 		= (x,y);
				x_diff 		= this.calcDistance(center_x, x);
				y_diff		= this.calcDistance(center_y, y);
				diff		= (y_diff * y_diff) + (x_diff * x_diff);
				if( diff <= brushsize*brushsize ):
					strength        = this.calcStrength( brushsize, sqrt(diff) );
					oldColor	= this.canvas.getColorAt(coords[0],coords[1]);
					if( oldColor[3] != 0 ):
						diff_r		= oldColor[0] - color[0];
						diff_g		= oldColor[1] - color[1];
						diff_b		= oldColor[2] - color[2];
						add_r		= diff_r/100*strength;
						add_g		= diff_g/100*strength;
						add_b		= diff_b/100*strength;
						new_r		= oldColor[0] - add_r;
						new_g		= oldColor[1] - add_g;
						new_b		= oldColor[2] - add_b;
						if(new_r > 255 ):	new_r = 255;
						if(new_r < 0 ):		new_r = 0;
						if(new_g > 255 ):	new_g = 255;
						if(new_g < 0 ):		new_g = 0;
						if(new_b > 255 ):	new_b = 255;
						if(new_b < 0 ):		new_b = 0;
						#print  str((new_r, new_g, new_b, 1)) + " " + str(oldColor)
						this.canvas.setColorAt(coords, (new_r, new_g, new_b,1),False,True);
		return True;
				
	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );

	def calcStrength( this, brushsize, distance ):
		if(brushsize == 0):
			return 100 - 100*distance
		return 100 - float(100/brushsize)*distance;

	def identifier(this):
		return "airbrush";
