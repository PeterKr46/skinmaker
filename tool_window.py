from Tkinter import *
from ttk import *
from tkColorChooser import askcolor
import sys

class ToolWindow:
	def __init__(this,parent):
		this.parent = parent;
		this.root = Tk();
		this.root.title("Tools - SkinMaker 2.5");
		this.root.resizable(0,0);
		#this.root.geometry("180x640")
		this.addElements();
		
	def addElements(this):
		this.WindowLabel	= Label(this.root, text="Available Brushes:");
		this.WindowLabel.grid(row=0,column=0,columnspan=2,sticky=W+E);
		
		this.BrushSelector 	= Listbox(this.root, height=18, width=29);
		this.BrushSelector.grid(row=1,column=0,columnspan=2,sticky=N+W+E);
		for brush in sorted(this.parent.brushes):
			this.BrushSelector.insert(END, brush);
		this.BrushSelector.bind("<ButtonRelease-1>",this.updateBrushSelection);
		
		this.BrushSizeFrame = Frame(this.root,borderwidth=2)
		this.BSSLabel		= Label(this.BrushSizeFrame, text="Brush size: 1", width=28);
		this.BSSLabel.grid(row=0,column=0,sticky=W+E);
		this.BrushSizeSlider = Scale(this.BrushSizeFrame, from_=0, to=31,orient=HORIZONTAL);
		this.BrushSizeSlider.grid(row=1,column=0,sticky=N+W+E);
		this.BrushSizeSlider.bind("<ButtonRelease-1>",this.updateBrushSize);
		this.BrushSizeSlider.bind("<B1-Motion>",this.updateBrushSize);
		this.BrushSizeFrame.grid(row=2,column=0,columnspan=2,sticky=W+E);
		
		this.ColorPreview	= Canvas(this.root,width=16,height=16,relief="solid",borderwidth=1,bg="#0000ff")
		this.ColorPreview.grid(row=3,column=0,sticky=W+N+S+E);
		this.ColorSelector	= Button(this.root,text="Select Color...", command= this.selectColor);
		this.ColorSelector.grid(row=3,column=1,sticky=W+N+S+E);
		
		this.BrushInfo		= Label(this.root, text=this.parent.brush.description);
		this.BrushInfo.grid(row=5, column=0,columnspan=2,sticky=W+E+N);
		
	def updateBrushSize(this,evt):
		this.BSSLabel.configure(text="Brush size: %s" % int(this.BrushSizeSlider.get() + 1));
		
	def updateBrushSelection(this,evt=""):
		selection = map(int, this.BrushSelector.curselection());
		if( len(selection) != 0 ):
			curBrush = this.BrushSelector.get(selection[0]);
			if( curBrush != this.parent.brush.identifier()):
				this.parent.selectBrush(curBrush);
				this.BrushInfo.configure(text=this.parent.brush.description);
		
	def updateColor(this):
		(r,g,b,a) = this.parent.scanvas.getColor()
		if( a == 0 ): return True;
		this.ColorPreview.create_rectangle(
			2,
			2,
			100,
			100,
			fill=this.parent.scanvas.toHex(r,g,b),
			outline="");
		
	def selectColor(this):
		newcolor = askcolor(color=this.parent.scanvas.toHex(this.parent.scanvas.color[0],this.parent.scanvas.color[1],this.parent.scanvas.color[2]))
		if( newcolor[0] == None ): return;
		(r,g,b) = newcolor[0];
		this.parent.scanvas.setColor((r,g,b,1));
		this.updateColor();

	def identifier(this):
		return "DEFAULT";
