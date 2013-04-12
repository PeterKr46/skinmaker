#===============| history_class.py |===============#

class History:
	def __init__(this):
		this.maxLength = 3;
		this.current_step_number = 0;
		this.history_list = [];
		this.current_step = [];
		
	def addChange(this, (x,y), before,after, silent=False):
##		print x,y,before,after
		if( silent == False):
			change = [(x,y), before, after];
			if( len(this.history_list) == this.maxLength ):
				this.history_list.pop(0);
			this.current_step.append(change);
			return True;
		change = [(x,y), before, after, True];
		if( len(this.history_list) == this.maxLength ):
			this.history_list.pop(0);
		this.current_step.append(change);
		
	def storeStep(this, evt = None):
		this.history_list.append(this.current_step);
		this.current_step = [];
		this.current_step_number += 1;
		if( this.current_step_number >= this.maxLength ): this.current_step_number = this.maxLength - 1;
		return True;
		
	def clear(this):
		this.current_step = [];
		this.history_list = [];
		
	def getLastStep(this):
		return this.history_list[this.current_step_number];
		
	def isInCurrentStep(this, x,y):
		for change in this.current_step:
			if( change[0] == (x,y) and not len(change) == 4): return True;
		return False;

	def undo(this):
		if( not this.canUndo()): return False
		this.current_step_number -= 1;

	def redo(this):
		if( not this.canRedo()): return False
		this.current_step_number += 1;

	def canUndo(this):
		if(this.current_step_number != 0): return True
		return False
	
	def canRedo(this):
		if(this.current_step_number != -1): return True
		return False
