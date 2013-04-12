# filler
from math import sqrt
from brush_class import Brush
from random import randint as random

class replacing(Brush):
	displayName	= "Color Replacement Tool";
	description	= "Replaces a color with the current color.";
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "BRUSH";
		this.displayName= "Color Replacement Tool"
		this.description= "Replaces a color with the current color."
		
        def leaveStamp(this, x, y): 
                if( not this.canvas.fits(x,y) ): return False;
                replaceColor		= this.canvas.getColorAt(x,y);
		brushsize               = this.canvas.getBrushSize();
                if( this.setColor == False):
                        color           = this.canvas.getColor();
                else:
                        color           = this.color;
     
                leftboundary    = x - brushsize;
                rightboundary   = x + brushsize + 1;
                topboundary             = y - brushsize;
                bottomboundary  = y + brushsize + 1;
     
                if( leftboundary        < 0             ): leftboundary         = 0;
                if( rightboundary       > 64    ): rightboundary        = 64; 
                if( topboundary         < 0     ): topboundary          = 0;
                if( bottomboundary      > 32    ): bottomboundary       = 32; 
     
                center_x,center_y = x,y;
                center_coords = (x,y);
     
                for x in range(leftboundary,rightboundary):
                        for y in range(topboundary,bottomboundary):
     
                                if( not this.canvas.fits(x,y) ): continue;
                                coords          = (x,y);
                                x_diff          = this.calcDistance(center_x, x); 
                                y_diff          = this.calcDistance(center_y, y); 
                                diff            = (y_diff * y_diff) + (x_diff * x_diff);
                                if( diff <= brushsize*brushsize and this.isColor(this.canvas.getColorAt(x, y), replaceColor) ):
                                        this.canvas.setColorAt( coords, color );
                return True;

	def isColor(this, color, control ):
		if not ( color[0] > control[0] - 5 and color[0] < control[0] + 5 ):
			return False;
		if not ( color[1] > control[1] - 5 and color[1] < control[1] + 5 ):
			return False;
		if not ( color[2] > control[2] - 5 and color[2] < control[2] + 5 ):
			return False;
		return True;

	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );
	       
