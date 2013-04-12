# !/usr/bin/python2.7
# -*- coding: utf-8 -*-
#================| __init__.py |================#
#--- Main File, also starter 			#
#--- Contained Classes:				#
#--- SkinMaker					#
#================| __init__.py |================#
#=================| importing |=================#
try:
	from Tkinter import *
except:
	from tkinter import *
from ttk import *
import tkFileDialog, tkMessageBox
import os, glob
import random

from PIL import Image, ImageDraw

from start_skin import startimage
from canvas_class import SCanvas
from brush_class import Brush
from stamp_class import Stamp
from tool_window import ToolWindow
from preview_window import PreviewWindow
from brushes import colorSelector
from brushes import eraser
from brushes import filler
from brushes import paintBrush
from brushes import replacing
from brushes import standardBrush
from brushes import airBrush
#==============| End of importing |=============#

global __version__
__version__ = "2.1.0"

class SkinMaker:

	def importAllBrushes(this):
		print "Loading Brushes...";
		this.brushes = {};
		this.brushes[colorSelector.colorSelector.displayName]	= colorSelector.colorSelector;
		this.brushes[eraser.eraser.displayName]	= eraser.eraser;
		this.brushes[filler.filler.displayName]	= filler.filler;
		this.brushes[paintBrush.paintBrush.displayName]	= paintBrush.paintBrush;
		this.brushes[replacing.replacing.displayName]	= replacing.replacing;
		this.brushes[standardBrush.standardBrush.displayName]	= standardBrush.standardBrush;		
		this.brushes[airBrush.airBrush.displayName] = airBrush.airBrush;
		print "Done. %s brush(es) loaded." % len(this.brushes);
		
	
	def __init__(this):
		# Main Window
		this.root = Tk();
		this.root.title("SkinMaker 2.5");
		this.root.protocol("WM_DELETE_WINDOW",this.exitProperly);
		this.root.resizable(0,0);
		
		
		# Import all Brushes
		this.importAllBrushes();
		
		# Tk Canvas object
		this.canvas = Canvas(this.root,width=640,height=320,relief="ridge",borderwidth=1,bg="white",cursor="cross");
		this.canvas.grid(row=1, column=1);

		# Mechanics Canvas Object
		this.scanvas = SCanvas(	this.canvas);
		
		# Default Brush
		this.brush = Brush(this.scanvas);
		
		# Prepare Menu
		this.menu = Menu(this.root);
		this.menu.add_command(label="Save as", command=this.saveDialog);
		this.menu.add_command(label="Load Skin", command=this.loadDialog);
		this.menu.add_command(label="Undo", command=this.scanvas.undoStep);
		this.menu.add_command(label="Redo");
		this.root.config(menu=this.menu);

		# Prepare all keybinds
		this.setKeyBinds();

		# Prepare Tool Window
		this.tools = ToolWindow(this);
		this.scanvas.tool_window = this.tools;
		this.tools.root.protocol("WM_DELETE_WINDOW",this.exitProperly);

		# Prepare Preview Window
		this.preview = PreviewWindow(this.scanvas.colors, this);
		this.preview.root.protocol("WM_DELETE_WINDOW",this.exitProperly);

		# Load start skin
		this.setImage(startimage);
		this.scanvas.drawOutline();

		# Launch UI
		this.root.mainloop();
		
	def setKeyBinds(this):
		this.canvas.bind("<ButtonRelease-1>",this.strokeEnd);
		this.canvas.bind("<Button-1>",this.onClick);
		this.canvas.bind("<B1-Motion>",this.onClick);
		
	def exitProperly(this):
		if(not tkMessageBox.askokcancel("Quit", "Are you sure you want to quit?") ): return;
		try: this.tools.root.destroy();
		except: foo = "bar";
		try: this.root.destroy();
		except: foo = "bar";
		try: this.preview.root.destroy();
		except: foo = "bar";
		print "Stopping...";
		print "Thank you for using the SkinMaker!";
		
	def onClick(this, evt):
		x,y = evt.x,evt.y;
		this.scanvas.setBrushSize(int(this.tools.BrushSizeSlider.get()));
		(x,y) = this.scanvas.gridValue(x,y);
		if(this.scanvas.fits(x,y)): 
			this.brush.leaveStamp(x,y)

	def randomColor(this):
		[r,g,b] = [random.randint(0,255) for x in range(3)]
		return (r,g,b,1);
		
	def strokeEnd(this,evt=""):
		this.preview.updatePixels(this.scanvas.colors);
		this.scanvas.history.storeStep();
	
	def brushExists(this, brushname):
		for key in sorted(this.brushes.keys()):
			if( key == brushname ): return True;
		return False;
		
	def selectBrush(this, brushname):
		if( not this.brushExists(brushname) ): return False;
		this.brush = this.brushes[brushname](this.scanvas);
	
	def setImage(this, image):
		this.scanvas.reset();
		try: imgpixels = image.load();
		except: return False;
		image.convert("RGBA");
		for x in range(image.size[0]):
			for y in range(image.size[1]):
				px = imgpixels[ x, y ];
				this.scanvas.setColorAt((x,y),(px[0],px[1],px[2],px[3]),True);
		this.preview.updatePixels(this.scanvas.colors);

	def loadDialog(this):
		path = tkFileDialog.askopenfilename();
		def validImage(path):
			try:
				Image.open(path);
				return True;
			except: return False;
		if( path == "" or path == None or path == ()): return;

		while( not validImage(path) ):
			#print path
			if( path == "" or path == None or path == ()):
				return;
			tkMessageBox.showinfo("Error opening file!", "The selected file is not a valid image file.");
			path = tkFileDialog.askopenfilename();
		this.setImage(Image.open(path));
		print "Loaded image '%s'." % path;

	def saveDialog(this):
		path = tkFileDialog.asksaveasfilename();
		if( path == "" or path == None): return;
		img = Image.new('RGBA', (64, 32), (0, 0, 0, 0));
		imgdraw = ImageDraw.Draw(img);
		for x in range(64):
			for y in range(32):
				color = this.scanvas.colors[x][y];
				if(color[3] == 0): continue;
				imgdraw.rectangle(( x, y, x, y), fill=this.scanvas.toHex(color[0], color[1], color[2]), outline=None);
		del imgdraw;
		img.save(path, "PNG");

print "SkinMaker v%s created by Peter Kramer" % __version__;
if( __name__ == '__main__'):		
	SM = SkinMaker();
