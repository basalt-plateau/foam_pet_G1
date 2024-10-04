



##
#

#
#
##


#/
#
import click
#
#
from foam_pet.adventures.sanique.venture import sanique_venture
from foam_pet.adventures.demux_hap.venture import demux_hap_venture
#
#
from foam_pet._essence import retrieve_essence
#
#
from ventures import ventures_map
#
#\


from foam_pet.adventures.harbor_basin import turn_on_harbor

def ventures_group ():
	essence = retrieve_essence ()

	@click.group ("offline_ventures")
	def group ():
		pass;
	
	
	@group.command ("start")
	def command__health ():	
		
		turn_on_harbor ({});
	
	
	return group;
	
	#/
	#
	#	This raises an exception if the "foam_pet_essence.py" is not yet built.
	#
	#
	try:
		from ventures.clique import ventures_clique
		group.add_command (ventures_clique ({
			"ventures": ventures_map ({
				"map": essence ["ventures"] ["path"],
				"ventures": [
					demux_hap_venture (),
					sanique_venture ()
				]
			})
		}))
		
		''''
		group.add_command (importlib.import_module ("ventures.clique").ventures_clique ({
			"ventures": retrieve_ventures ()
		}))
		"'''
		
		from foam_pet.adventures.demux_hap._plays._clique import demux_hap_clique
		group.add_command (demux_hap_clique ())
		
	except Exception as E:
		print ("venture import exception:", E)

	return group




#



