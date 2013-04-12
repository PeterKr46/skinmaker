# standardBrush
import random
from brush_class import Brush

class randomBrush(Brush):
	displayName	= "(Almost) Random Brush."
	description	= "Double Rainbow all the way!!!"
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= True;
		this.startcolor = (random.randint(0,250),random.randint(0,250),random.randint(0,250),1);
		this.color 		= (random.randint(0,250),random.randint(0,250),random.randint(0,250),1);
		this.type 		= "BRUSH";
		this.displayName= "(Almost) Random Brush."
		this.description= "Double Rainbow all the way!!!"
		
	def leaveStamp(this, x, y):
		if( not this.canvas.fits(x,y) ): return False;
		brushsize		= this.canvas.getBrushSize();
		(r,g,b,a) 		= this.color;
		r 			   += random.randint(0,50);
		g 			   += random.randint(0,50);
		b 			   += random.randint(0,50);
		if( r > 255 ): 	r = this.startcolor[0];
		if( g > 255 ): 	g = this.startcolor[1];
		if( b > 255 ): 	b = this.startcolor[2];
		color 			= (r,g,b,a);
		this.color 		= (r,g,b,a);
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
					this.canvas.setColorAt( coords, color );
		return True;
				
	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );

	def identifier(this):
		return "randomBrush";
