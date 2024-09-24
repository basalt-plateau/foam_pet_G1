
'''
	from vaccines.adventures.sanique._controls.off import turn_off_sanique
	turn_off_sanique ()
'''


'''
	sanic inspect shutdown
'''


'''
	objectives:
		[ ] implicit
'''

#/
#
from biotech.topics.show.variable import show_variable
#
#
import multiprocessing
import subprocess
import time
import os
import atexit
import pathlib
from os.path import dirname, join, normpath
import sys
#
#\

def background (procedure, CWD):
	show_variable ("procedure:", procedure)
	process = subprocess.Popen (procedure, cwd = CWD)

def turn_off_sanique (packet):
	inspector_port = str (packet ["ports"] ["inspector"])

	def actually ():
		harbor_path = str (normpath (join (
			pathlib.Path (__file__).parent.resolve (), 
			".."
		))) 
		
		#host = physics ["sanique"] ["inspector"] ["host"]
		#port = physics ["sanique"] ["inspector"] ["port"]
		#URL = f"http://{ host }:{ port }"
		
		process = background (
			procedure = [
				"sanic",
				"inspect",
				"shutdown",
				f"--port",
				str (inspector_port),
				
				
			],
			CWD = harbor_path
		)
		
	return actually;
