# colorselector
from math import sqrt	
from brush_class import Brush
from random import randint as random

class colorSelector(Brush):
	displayName	= "Color Picker"
	description	= "Selects a color from the Canvas";
	type 		= "TOOL";
	cursor		= "target";
	
	def __init__(this, canvasobject):
		this.canvas 	= canvasobject;
		this.setColor 	= False;
		this.color 		= None;
		this.type 		= "TOOL";
		this.displayName= "Color Picker";
		this.description= "Selects a color from the Canvas";
		
	def leaveStamp(this, x, y):
		if(not this.canvas.getColorAt(x,y)[3] == 0):
			this.canvas.setColor(this.canvas.getColorAt(x,y));
			this.canvas.tool_window.updateColor();
		return True;

	def identifier(this):
		return "colorSelector";
