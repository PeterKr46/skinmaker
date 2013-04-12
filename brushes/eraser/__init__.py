# standardBrush
import os,sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
	
from brush_class import Brush

class eraser(Brush):
	displayName	= "Eraser";
	description	= "Erases parts of your skin.";
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "BRUSH";
		this.displayName= "Eraser"
		this.description= "Erases parts of your skin."
		
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
					this.canvas.eraseColorAt(x,y);
		return True;
				
	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );

	def identifier(this):
		return "standardBrush";
