# filler
import os,sys
from math import sqrt
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
	
from brush_class import Brush
from random import randint as random

class filler(Brush):
	displayName	= "Filling Tool";
	description	= "Fills areas of the same color.";
	type 		= "BRUSH";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "BRUSH";
		this.displayName= "Filling Tool"
		this.description= "Fills areas of the same color."
		this.filled		= [];
		
	def leaveStamp(this, x, y):
		if( not this.canvas.fits(x,y) ): return False;
		brushsize		= this.canvas.getBrushSize();
		if( this.setColor == False):
			color		= this.canvas.getColor();
		else:
			color 		= this.color;
		try:
			this.fillPixel((x,y),this.canvas.getColorAt(x,y));
		except:
			this.filled = [];
		return True;

	def identifier(this):
		return "paintBrush";
		
	def fillPixel(this, coords, searchedcolor):
		(x,y) = coords;
		this.canvas.setColorAt((x,y),this.canvas.getColor());
		for (xt, yt) in this.getNeighbors(x,y):
			if( not this.canvas.fits( xt,yt) ): 					continue;
			if( this.wasUsed(xt,yt) ): 								continue;
			if( this.canvas.getColorAt( xt,yt ) != searchedcolor ): continue;
			this.fillPixel( (xt,yt), searchedcolor);
			
		
	def getNeighbors(this,x,y):
		return [(x+1,y),(x,y+1),(x-1,y),(x,y-1)];
		
	def wasUsed(this,x,y):
		for px in this.filled:
			(xt,yt) = px;
			if( x == xt and y == yt ): return True;
			
		return False;
