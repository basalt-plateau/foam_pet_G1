









''''
	
	@ story 1
	
"'''





from os.path import dirname, join, normpath
import sys
import pathlib
import os

this_directory = pathlib.Path (__file__).parent.resolve ()	
CWD = str (normpath (join (this_directory, "Move")))
os.chdir (CWD)

#\
#/


import click
from story_plays import story_plays

''''
	@ founder
		@ soil
"'''


from story_theme import story_theme
theme = story_theme ();
founder = theme ["founder"]
module_name = theme ["module_name"]




screenplay_compile = " ".join ([
	"aptos move compile",
	f'--named-addresses founder={ founder }'
])
screenplay_publish = " ".join ([
	"aptos move publish",
	'--url "https://api.devnet.aptoslabs.com/v1"',
	'--assume-yes',
	f'--named-addresses founder={ founder }'			
])

def clique ():
	@click.group ()
	def group ():
		pass

	@click.command ("compile")
	def command_compile ():	
		screenplays = [
			"rm -rf build",
			screenplay_compile
		]
		for screenplay in screenplays:
			print ("screenplay:", screenplay)
			os.system (screenplay)
	group.add_command (command_compile)

	#
	#
	#	https://aptos.dev/en/build/smart-contracts/error-codes
	#
	#
	@click.command ("publish")
	def publish ():	
		
		screenplays = [
			# "rm -rf .aptos",
			"rm -rf build",
			screenplay_compile,
			screenplay_publish
		]
		for screenplay in screenplays:
			print ("screenplay:", screenplay)
			os.system (screenplay)
	group.add_command (publish)
	
	

	
	group.add_command (story_plays ())
	
	group ()


clique ()
