#===============| stamp_class.py |===============#
from brush_class import Brush

class Stamp(Brush):
	def __init__(this,canvasobject):
		this.canvas 		= canvasobject;
		this.setColor 		= True;
		this.type 			= "STAMP";
		this.pixels			= 	[
									[(0,0,0,0),(0,0,0,1),(0,0,0,0)],
									[(0,0,255,1),(0,0,0,0),(0,0,0,1)],
								];
		this.stampCenter	= (1,1); 
		
	def leaveStamp(this, x, y):
		if( not this.canvas.fits(x,y) ): return False;
		center_x,center_y = x,y;
		x, y = 0, 0;
		for row in this.pixels:
			for color in row:
				x += 1;
				if( color[3] == 0 ): continue;
				if( this.canvas.fits(x,y) ):
					this.canvas.setColorAt((center_x + x - this.stampCenter[0],center_y + y - this.stampCenter[1]), color);
			y += 1;
			x = 0;
		return True;
				
				
	def calcDistance(this, f1, f2):
		if( f1 - f2 >= 0 ):
			return f1 - f2;
		return -1 * ( f1 - f2 );
