









import os
import click

from story_theme import story_theme
theme = story_theme ();
pilot = theme ["pilot"]
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
	#	aptos move activity_create --address "0xd3f5a67384c9687138b49153a19450216d2c7be6f7f9595eabe27336c7ca072e"
	#
	#	./story views account_has_emblem --address "0xd3f5a67384c9687138b49153a19450216d2c7be6f7f9595eabe27336c7ca072e"
	#
	#
	@group.command ("account_has_emblem")
	@click.option ('--address', required = True)
	def account_has_emblem (address):	
		# address = pilot
	
		screenplay = " ".join ([
			"aptos move view",
			'--assume-yes',
			f"--function-id { pilot }::{ module_name }::account_has_emblem",
			build_args ([
				f"address:{ address }"
			])
		])
		
		print ("screenplay:", screenplay)
		os.system (screenplay)
		

		

	return group