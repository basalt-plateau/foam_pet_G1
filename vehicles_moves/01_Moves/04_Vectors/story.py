









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

''''
	@ founder
		@ soil
"'''


''''
	given:
		module soil::module_7 {}
		module_name = "module_7"
"'''
module_name = "counter_with_goals_5"

founder = "95547730EBE9325C0B7E04A1C3A12A2C8061FF2B70A566886F1A19702B5F7C82"
vehicle_2 = "6AF55AFB070E2127F55097C1F0516949A04B53DD022FD1AAAE155D21E988E212"
vehicle_3 = "95547730EBE9325C0B7E04A1C3A12A2C8061FF2B70A566886F1A19702B5F7C82"

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
	
	
	
	#
	#
	#	aptos move activity_create
	#
	#
	@click.command ("activity_create")
	def activity_create ():	
		fun = "create"
		
		amount = "10"
		
		args = build_args ([
			f'u64:{ amount }',
		])
		
		screenplay = " ".join ([
			"aptos move run",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::{ fun }",
			args
		])
		print ("screenplay:", screenplay)
		os.system (screenplay)
	group.add_command (activity_create)
		
		
		
	#
	#
	#	aptos move activity_increment
	#
	#
	@click.command ("activity_increment")
	def activity_increment ():	
		fun = "increment_goal"
		screenplay = " ".join ([
			"aptos move run",
			'--assume-yes',
			f"--function-id { founder }::{ module_name }::{ fun }"
		])
		print ("screenplay:", screenplay)
		os.system (screenplay)
		
		
	group.add_command (activity_increment)
	
	
	group ()


clique ()
