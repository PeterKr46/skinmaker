from Tkinter import *
from ttk import *
from tkColorChooser import askcolor

class PreviewWindow():
	
	def __init__(this, pixels, parent):
		this.offset = 2;
		this.parent = parent;
		this.root = Tk();
		this.root.title("SkinMaker Preview Window");
		this.root.resizable(0,0);
		this.prepCanvas();
		this.updatePixels(pixels);

	def prepCanvas( this ):
		this.canvas = Canvas( this.root,width=580,height=340,relief="solid",borderwidth=1,bg="#121212");
		this.canvas.grid(row=0,column=0,sticky=W+N+S+E);
		for x in range(58):
			for y in range(34):
				this.setPixel(x,y,(0,0,0,0));

	def updatePixels( this, pixels ):
		# Face Front
		for x in range( 8,16):
			for y in range( 8,16):
				this.setPixel( x-2, y-6, pixels[x][y] );
	
		# Face Left
		for x in range( 0, 8):
			for y in range( 8,16):
				this.setPixel( x+48, y-6, pixels[x][y] );

		# Face Back
		for x in range(24,32):
			for y in range( 8,16):
				this.setPixel( x+10, y-6, pixels[x][y] );
		# Face Right
		for x in range(16,24):
			for y in range(8,16):
				this.setPixel( x+4, y-6, pixels[x][y] );
		
		# Body Font
		for x in range(20,28):
			for y in range(20,32):
				this.setPixel( x-14, y-10, pixels[x][y] );
		
		# Body Back
		for x in range(32,40):
			for y in range(20,32):
				this.setPixel( x+2, y-10, pixels[x][y] );
		
		# Arm Front Left
		for x in range(44,48):
			for y in range(20,32):
				this.setPixel( x-42, y-10, pixels[x][y] );

		# Arm Front Right
		for y in range(20,32):
			for x in range(44,48):
				this.setPixel( (48-x+44)-31, y-10, pixels[x][y] );

		# Arm Back Left
		for x in range(52,56):
			for y in range(20,32):
				this.setPixel( x-22, y-10, pixels[x][y] );
		
		# Arm Back Right
		for x in range(52,56):
			for y in range(20,32):
				this.setPixel( (56-x+52)-11, y-10, pixels[x][y] );
		
		# Arm Outside Left
		for x in range(40,44):
			for y in range(20,32):
				this.setPixel( x-18, y-10, pixels[x][y] );

		# Arm Outside Right
		for x in range(40,44):
			for y in range(20,32):
				this.setPixel( (44-x+40)+9, y-10, pixels[x][y] );

		# Helmet Front
                for x in range(40,48):
			for y in range(8,16):
				this.setPixel( x-34, y-6, pixels[x][y],True );
		
		# Helmet Left
                for x in range(32,40):
			for y in range(8,16):
				this.setPixel( x+16, y-6, pixels[x][y],True );
		
		# Helmet Back
                for x in range(56,64):
			for y in range(8,16):
				this.setPixel( x-22, y-6, pixels[x][y],True );
		
		# Helmet Right
                for x in range(48,56):
			for y in range(8,16):
				this.setPixel( x-28, y-6, pixels[x][y],True);
		
		# Leg Front Left
		for x in range(4,8):
			for y in range(20,32):
				this.setPixel( x+2, y+2, pixels[x][y]);

		# Leg Front Right
		for x in range(4,8):
			for y in range(20,32):
				this.setPixel( (4-x+8)+5, y+2, pixels[x][y]);

		# Leg Outside Left
		for x in range(0,4):
			for y in range(20,32):
				this.setPixel( x+50, y+2, pixels[x][y]);
		
		# Leg Outside Right
		for x in range(4):
			for y in range(20,32):
				this.setPixel( (0-x+4)+21,y+2,pixels[x][y]);

		# Leg Back Left
		for x in range(12,16):
			for y in range(20,32):
				this.setPixel( x+22,y+2,pixels[x][y]);

		# Leg Back Right
		for x in range(12,16):
			for y in range(20,32):
				this.setPixel( (12-x+16)+25, y+2, pixels[x][y]);

	def setPixel( this, x, y, (r,g,b,a), ignoreTransparency=False):
		if( a == 0 and ignoreTransparency == False):
			this.canvas.create_rectangle(x*10+this.offset, y*10+this.offset, x*10+10+this.offset, y*10+10+this.offset, fill="#aaaaaa", outline="");
			this.canvas.create_rectangle(x*10+5+this.offset, y*10+this.offset, x*10+10+this.offset, y*10+5+this.offset, fill="#555555", outline="");
			this.canvas.create_rectangle(x*10+this.offset, y*10+5+this.offset, x*10+5+this.offset, y*10+10+this.offset, fill="#555555", outline="");
			return;
		elif( a == 0 and ignoreTransparency == True):
			return;
		this.canvas.create_rectangle(
			x * 10 + this.offset,  y * 10 + this.offset,
			x * 10 + 10 + this.offset, y * 10 + 10 + this.offset,
			fill=this.parent.scanvas.toHex(r,g,b),
			outline="");
	
	def inRange( this, x, y ):
		if( x < 0 or x > 28 or y < 0 or y > 17 ): return False
		return True;
