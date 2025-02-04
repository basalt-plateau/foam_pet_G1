

'''
	from foam_pet.adventures.demux._controls.on import turn_on_demux_hap
'''

import foam_pet.adventures.demux_hap.SSL as HA_SSL
import foam_pet.adventures.demux_hap.configs.HTTPS_to_HTTP as HA_HTTPS_to_HTTP
from .build import build_demux_certificates

from foam_pet._essence import retrieve_essence
	

import os

def turn_on_demux_hap ():
	essence = retrieve_essence ()
	
	to_address = essence ["demux_hap"] ["to"]
	
	if (essence ["demux_hap"] ["build self signed certs"] == "yes"):
		build_demux_certificates ()

	config_path = "/etc/haproxy/haproxy.cfg"
	
	HA_HTTPS_to_HTTP.build (
		SSL_certificate_path = "/etc/haproxy/SSL/certificate.pem",
		config_path = config_path,
		
		to_addresses = [
			to_address,
			to_address,
			to_address,
			to_address,
			to_address,
			to_address,
			to_address,
			to_address
		]
	)
	
	
	
	#
	#	Check that the config is good
	#
	#
	os.system (f"haproxy -f '{ config_path }' -c")
	#os.system (f"cat '{ config_path }'")
	
	os.system ("service haproxy start")
	#os.system ("service haproxy status")
	
	if (False):
		os.system ("systemctl restart haproxy")
		os.system ("systemctl status haproxy -l --no-pager")
		
	
