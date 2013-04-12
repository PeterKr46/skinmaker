#===============| canvas_class.py |===============#
from history_class import History

class SCanvas:

	def __init__(this, visualcanvas):
		this.canvas		 	= visualcanvas;
		this.history 		= History();
		this.color			= (0,0,255,1);
		this.offset			= 3;
		this.width 			= 64;
		this.height 		= 32;
		this.brushsize		= 3;
		this.colors 		= [[(0,0,0,0) for y in range(32) ] for x in range(64) ];
		this.pixels 		=	[
							[
								this.canvas.create_rectangle(
									x*10 + this.offset,
									y*10 + this.offset,
									x*10+10 + this.offset,
									y*10+10 + this.offset,
									fill="#ffffff",
									outline="")
									for y in range(33)
							]
							for x in range(65)
						];
		this.reset();
	
	def reset( this ):
		for x in range(64):
			for y in range(32):
				this.eraseColorAt(x,y,True);
		this.drawOutline();

	def setColorAt(this, (x, y), rgba, silent= False, ignoreHistory=False):
		if( len( rgba ) != 4 ):				return False;
		if( this.fits( x, y ) != True ): 		return False;
		if( this.history.isInCurrentStep(x,y) and ignoreHistory == False ):	return False;
		if( rgba[3] == 0):
			this.eraseColorAt(x,y,silent);
		if(rgba[3] > 0 ):
			rgba = (rgba[0], rgba[1], rgba[2], 1);
		oldColor = this.getColorAt(x,y);
		this.colors[x][y] = rgba;
		(r,g,b,a) = rgba;
		if(a >= 1):
			pixelId 	= this.pixels[x][y];
			this.canvas.create_rectangle(
				x*10 + this.offset,
				y*10 + this.offset,
				x*10+10 + this.offset,
				y*10+10 + this.offset,
				fill=this.toHex(r,g,b),
				outline="");
		if( silent == False): this.history.addChange((x,y),oldColor,rgba);
		else: this.history.addChange((x,y),oldColor,rgba, True);
		return True;
		# TODO: Try using color changes instead of overlaying old rectangle.
		
	def setColor(this, rgba):
		if( len(rgba) != 4 ): return False;
		this.color = rgba;
		return True;
		
	def getColorAt(this,x ,y ):
		return this.colors[x][y];
		
	def isTransparent(this, x, y):
		if( this.colors[x][y][3] == 0):
			return True;
		return False;
		
	def fits(this, x, y):
		if( x < 0 or x >= this.width  ): return False;
		if( y < 0 or y >= this.height ): return False;
		return True;
	
	def gridValue(this, x, y):
		x,y = (x)/10,(y)/10;
		return (x,y);
		
	def toHex(this, r, g, b):
		hexchars = "0123456789ABCDEF"
		return "#" + hexchars[int(r / 16)] + hexchars[int(r % 16)] + hexchars[int(g / 16)] + hexchars[int(g % 16)] + hexchars[int(b / 16)] + hexchars[int(b % 16)]
	
	def getBrushSize(this):
		return this.brushsize;
		
	def setBrushSize(this,size):
		this.brushsize = size;
		
	def getColor(this):
		return this.color;
	
	
	def eraseColorAt(this, x, y, silent= False):
		if( this.fits( x, y ) != True ): 		return False;
		if( this.history.isInCurrentStep(x,y) ):	return False;
		oldColor = this.getColorAt(x,y);
		this.colors[x][y] = (0,0,0,0);
		this.canvas.create_rectangle(x*10+this.offset, y*10+this.offset, x*10+10+this.offset, y*10+10+this.offset, fill="#aaaaaa", outline="");
		this.canvas.create_rectangle(x*10+5+this.offset, y*10+this.offset, x*10+10+this.offset, y*10+5+this.offset, fill="#555555", outline="");
		this.canvas.create_rectangle(x*10+this.offset, y*10+5+this.offset, x*10+5+this.offset, y*10+10+this.offset, fill="#555555", outline="");
		if( silent == False): this.history.addChange((x,y),oldColor,(0,0,0,0));
		else: this.history.addChange((x,y),oldColor,(0,0,0,0), True);
		
	def undoStep(this):
		if not(this.history.canUndo()):
			return False
		for action in history.getLastStep():
			x,y	= action[0]
			before	= action[1]
			after	= action[2]
			this.setColorAt((x,y),before,True);
		this.history.undo()
		return True

	def drawOutline(this):
		for x in range(8):
			for y in range(8):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(24,40):
			for y in range(8):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(56,64):
			for y in range(8):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(4):
			for y in range(16,20):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(12,20):
			for y in range(16,20):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(36,44):
			for y in range(16,20):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(52,64):
			for y in range(16,20):
				this.setColorAt((x,y), (0,0,0,1), True, True);
		for x in range(56,64):
			for y in range(20,32):
				this.setColorAt((x,y), (0,0,0,1), True, True);
