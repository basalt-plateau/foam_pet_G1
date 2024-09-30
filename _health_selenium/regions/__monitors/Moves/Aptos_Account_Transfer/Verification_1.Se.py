





#
#	python3 health.proc.py run --path="Moves/Aptos_Account_Transfer/Verification_1.Se.py"
#

''''
	* open the ICAN Domain Address
	
	* change the inputs:
		* devnet
"'''



#\
#
import traceback
import json
import time
import multiprocessing
import concurrent.futures
#
#
from selenium.webdriver.common.by import By
#
#
from vivaciousness._plays import retrieve_plays
#
from vivaciousness.Moves.Aptos_Account_Transfer.Friends.open_modal import open_friends_modal
from vivaciousness.Moves.Aptos_Account_Transfer.Friends.make_petition import make_petition
from vivaciousness.Moves.Aptos_Account_Transfer.Friends.petition_suggestion import petition_suggestion
#
from vivaciousness.Moves.Aptos_Account_Transfer.Relatives.open_modal import open_relatives_modal
from vivaciousness.Moves.Aptos_Account_Transfer.Relatives.make_signature import make_signature
#
from vivaciousness.health_regions.connect import connect_to_driver
from vivaciousness.health_regions.physics import derive_physics
from vivaciousness.procedures.Faucet.Give import give_Octas_from_faucet
from vivaciousness.procedures.loop import loop
from vivaciousness.accounts import ask_for_accounts
from vivaciousness.regions.Seeds.Features.change_net import change_net
from vivaciousness.Milieus.navigate import Milieus_Navigate
#
from vivaciousness.memo import proceed_through_memo
#
#/

from vivaciousness.Moves.Aptos_Account_Transfer.vacation import throw_APT_vacation



def goto_address (driver_1, driver_1_ICAN_DNS_Address):
	driver_1.get (driver_1_ICAN_DNS_Address)
	


''''
monitor_throw ({
	"friends": {
		"captain": "",
		
		"origin address": "",
		"to address": "",
		"amount APT": "",
	},
	"relatives": {
		"captain": "",
		
		"origin address private key": ""
	}
})
"'''
def monitor_throw (packet):
	give_Octas_from_faucet ({
		"icann_faucet_net_address": "https://faucet.devnet.aptoslabs.com/mint",
		"amount_of_octas": "1e8",
		"to_address": packet ["friends"] ["origin address"]
	})

	plays = retrieve_plays ()
	URL = plays ["URL"]
	
	friends_captain = connect_to_driver ();
	friends_captain.get (URL)
	proceed_through_memo ({ "driver": friends_captain });
	
	relatives_captain = connect_to_driver ();
	relatives_captain.get (URL)
	proceed_through_memo ({ "driver": relatives_captain });

	#\
	#
	#	Relatives Modal
	#
	#
	change_net ({
		"driver": packet ["relatives"] ["captain"],
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ relatives_modal_navigation_buttons ] = open_relatives_modal ({
		"tailfin": packet ["relatives"] ["captain"],
		"ICAN_DNS_Address": ""
	})
	#/
	
	#\
	#
	#	Friends Modal: Open
	#
	#
	change_net ({
		"driver": friends_captain,
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ friends_modal_navigation_buttons ] = open_friends_modal ({
		"driver": friends_captain,
		"ICAN_DNS_Address": ""
	})
	#
	#/

	#\
	#
	#	Friends Petition
	#
	#
	[ petition_hexadecimal_string ] = make_petition ({
		"driver_1": friends_captain,
		
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"address_from": packet ["friends"] ["origin address"],
		"address_to": packet ["friends"] ["to address"],
		"amount_APT": packet ["friends"] ["amount APT"]
	});
	friends_modal_navigation_buttons ["next"].click ()
	#/
	
	#\
	#
	#	Relatives Signature
	#
	#
	[ signature_hexadecimal_string ] = make_signature ({
		"tailfin": relatives_captain,
		"relatives_modal_navigation_buttons": relatives_modal_navigation_buttons,
		
		"petition_hexadecimal_string": petition_hexadecimal_string,
		"origin_private_key": packet ["relatives"] ["origin address private key"]
	})
	#/
	
	
	#\
	#
	#	Friends Suggestion
	#
	#
	petition_suggestion ({
		"tailfin": friends_captain,
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"signature_hexadecimal_string": signature_hexadecimal_string
	});
	#/
	
	
	
	
def check_1 ():
	plays = retrieve_plays ();
	
	##
	#
	accounts = plays ["accounts"]
	#
	origin_address = accounts ["1"] ["address"]
	origin_private_key = accounts ["1"] ["private key"]
	#
	address_to = accounts ["2"] ["address"]
	#
	##
	
	throw_APT_vacation ({
		"friends": {
			"origin address": origin_address,
			"to address": address_to,
			"amount APT": "0.01",
		},
		"relatives": {
			"origin address private key": origin_private_key
		}
	})

	
checks = {
	'check 1': check_1
}