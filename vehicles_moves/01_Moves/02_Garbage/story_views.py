









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



def story_views ():
	@click.group ("views")
	def group ():
		pass



		
	#
	#
	#	aptos move activity_create
	#
	#
	@group.command ("ask_address_landfill_size")
	def activity_create ():	
		address = founder
	
		screenplay = " ".join ([
			"aptos move view",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::ask_address_landfill_size",
			build_args ([
				f"address:{ address }"
			])
		])
		
		print ("screenplay:", screenplay)
		os.system (screenplay)
		

		

	return group