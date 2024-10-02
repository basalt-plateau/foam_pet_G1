





import os
import click

from story_theme import story_theme
theme = story_theme ();
founder = theme ["founder"]
module_name = theme ["module_name"]



def build_type_args (bracket):
	if (len (bracket) >= 1):
		return ' '.join ([
			f'--type-args',
			* bracket
		])

	return ''
	
def build_args (bracket):
	if (len (bracket) >= 1):
		return ' '.join ([
			f'--args',
			* bracket
		])

	return ''



def story_plays ():
	@click.group ("plays")
	def group ():
		pass


	#
	#
	#	build_global_landfill
	#
	#
	@group.command ("build_global_landfill")
	def build_global_landfill ():	
		screenplay = " ".join ([
			"aptos move run",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::build_global_landfill",
			build_args ([])
		])
		
		print ("screenplay:", screenplay)
		os.system (screenplay)
		
	
	#
	#
	#	remove_garbage_from_landfill
	#
	#
	@group.command ("remove_garbage_from_landfill")
	def remove_garbage_from_landfill ():	
		screenplay = " ".join ([
			"aptos move run",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::remove_garbage_from_landfill",
			build_args ([])
		])
		
		print ("screenplay:", screenplay)
		os.system (screenplay)
	
		
	#
	#
	#	aptos move activity_increment
	#
	#
	@group.command ("add_garbage_to_landfill")
	def add_garbage_to_landfill ():	
		screenplay = " ".join ([
			"aptos move run",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::add_garbage_to_landfill"
		])
		
		print ("screenplay:", screenplay)
		os.system (screenplay)
		
		

	return group