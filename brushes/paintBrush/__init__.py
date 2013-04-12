# paintBrush
import os,sys
from math import sqrt
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
	
from brush_class import Brush
from random import randint as random

class paintBrush(Brush):
	displayName	= "Paint Brush"
	description	= "Smoother than the standard brush."
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "BRUSH";
		this.displayName= "Paint Brush"
		this.description= "Smoother than the standard brush"
		
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
				sqrbs		= brushsize*brushsize;
				if( diff <= sqrbs ):
					this.canvas.setColorAt( coords, this.getCloseColor(color) );
				elif( sqrt(diff) -0.75 <= sqrt(sqrbs) ):
					(r,g,b,a) = this.getCloseColor(this.canvas.getColorAt( x, y ));
					if( a == 0): continue;
					(r2,g2,b2,a) = color;
					this.canvas.setColorAt( coords, ((r + r2)/2, (g + g2)/2, (b + b2)/2, a),True );
		return True;
				
	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );

	def identifier(this):
		return "paintBrush";
	
				
	def getCloseColor(this, rgba):
		(r,g,b,a) = rgba;
		if( a == 0 ): return (0,0,0,0);
		r += random(-2,2);
		g += random(-2,5);
		b += random(-2,2);
		if( r < 0 ): r = 0;
		if( g < 0 ): g = 0;
		if( b < 0 ): b = 0;
		if( r > 255 ): r = 255;
		if( g > 255 ): g = 255;
		if( b > 255 ): b = 255;
		a = 1;
		return (r,g,b,a);
