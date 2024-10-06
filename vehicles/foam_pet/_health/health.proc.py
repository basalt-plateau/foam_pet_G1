

'''
	mongo connection strings
		
		DB: foam_pet
			
			collection: 
				cautionary_ingredients
				essential_nutrients
'''

''''
	https://github.com/jonhoo/fantoccini
"'''

import pathlib
from os.path import dirname, join, normpath
import sys
def add_paths_to_system (paths):
	this_directory = pathlib.Path (__file__).parent.resolve ()	
	for path in paths:
		sys.path.insert (0, normpath (join (this_directory, path)))
	

add_paths_to_system ([
	'/Metro/vehicles'
])


#----
#
import Emergency
#
#
import rich
#
#
import json
import pathlib
from os.path import dirname, join, normpath
import os
import sys
import subprocess
#
#
from foam_pet._health import monitor_health
#
#----

#----
#
name = "foam_pet"
this_directory = pathlib.Path (__file__).parent.resolve ()

vehicles = "/Metro/vehicles"
this_vehicle = str (normpath (join (vehicles, f"foam_pet")))

if (len (sys.argv) >= 2):
	glob_string = this_vehicle + '/' + sys.argv [1]
	db_directory = False
else:
	glob_string = this_vehicle + '/**/status_*.py'
	db_directory = normpath (join (this_directory, "DB"))

print ("glob string:", glob_string)
#
#----

monitor_health ({
	"glob_string": glob_string,
	"vehicles": vehicles,
	"this_vehicle": this_vehicle,
	"db_directory": db_directory
})


