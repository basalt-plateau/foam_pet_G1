





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
#from vivaciousness.Moves.Aptos_Account_Transfer.friends_driver_ask import friends_driver_ask
#from vivaciousness.Moves.Aptos_Account_Transfer.relatives_driver.build_signed_transaction import build_ST_with_relatives
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

	
def goto_address (driver_1, driver_1_ICAN_DNS_Address):
	driver_1.get (driver_1_ICAN_DNS_Address)
	

	
def check_1 ():
	plays = retrieve_plays ();
	accounts = plays ["accounts"]

	origin_address = accounts ["1"] ["address"]
	origin_private_key = accounts ["1"] ["private key"]
	
	address_to = accounts ["2"] ["address"]
	
	give_Octas_from_faucet ({
		"icann_faucet_net_address": "https://faucet.devnet.aptoslabs.com/mint",
		"amount_of_octas": "1e8",
		"to_address": origin_address
	})
	
	friends_driver = connect_to_driver ();
	relatives_driver = connect_to_driver ();	
	
	plays = retrieve_plays ()
	URL = plays ["URL"]
	
	friends_driver.get (URL)
	proceed_through_memo ({ "driver": friends_driver });
	
	relatives_driver.get (URL)
	proceed_through_memo ({ "driver": relatives_driver });
	
	#\
	#
	#	Relatives Modal
	#
	#
	change_net ({
		"driver": relatives_driver,
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ relatives_modal_navigation_buttons ] = open_relatives_modal ({
		"tailfin": relatives_driver,
		"ICAN_DNS_Address": ""
	})
	#/

	
	#\
	#
	#	Friends Modal
	#
	#
	change_net ({
		"driver": friends_driver,
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ friends_modal_navigation_buttons ] = open_friends_modal ({
		"driver": friends_driver,
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
		"driver_1": friends_driver,
		
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"address_from": origin_address,
		"address_to": address_to
	});
	friends_modal_navigation_buttons ["next"].click ()
	#/
	
	#\
	#
	#	Relatives Signature
	#
	#
	[ signature_hexadecimal_string ] = make_signature ({
		"tailfin": relatives_driver,
		"relatives_modal_navigation_buttons": relatives_modal_navigation_buttons,
		
		"petition_hexadecimal_string": petition_hexadecimal_string,
		"origin_private_key": origin_private_key
	})
	#/
	
	
	#\
	#
	#	Friends Suggestion
	#
	#
	petition_suggestion ({
		"tailfin": friends_driver,
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"signature_hexadecimal_string": signature_hexadecimal_string
	});
	#/
	
	
	return;
	
	
	''''
	[ signature_hexadecimal_string ] = build_ST_with_relatives ({
		"driver_2": relatives_driver,
		"driver_2_ICAN_DNS_Address": driver_2_ICAN_DNS_Address,
		
		"unsigned_transaction_hexadecimal_string": unsigned_transaction_hexadecimal_string,
		"account_1": accounts ["1"]
	})
	
	friends_driver_ask ({
		"driver_1": friends_driver,
		"signature_hexadecimal_string": signature_hexadecimal_string,
		"inner_modal_buttons": inner_friends_modal_buttons
	})
	"'''
	
	
	
	
checks = {
	'check 1': check_1
}