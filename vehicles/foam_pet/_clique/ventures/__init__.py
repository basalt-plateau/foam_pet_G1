



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
from foam_pet._essence import turn_off_external_essence
	

def ventures_group ():
	# essence = retrieve_essence ()

	@click.group ("offline_ventures")
	def group ():
		pass;
	
	
	@group.command ("start")
	def command__health ():	
		turn_off_external_essence ()
		turn_on_harbor ({});
	
	
	return group;






#



