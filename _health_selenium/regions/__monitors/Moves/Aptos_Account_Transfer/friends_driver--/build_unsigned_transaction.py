

#/
#
from .UT_Object import check_UT_Object
#
from vivaciousness.health_regions.connect import connect_to_driver
from vivaciousness.procedures.Faucet.Give import give_Octas_from_faucet
from vivaciousness.procedures.loop import loop
#
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#
#
import traceback
import json
import time
import multiprocessing
import concurrent.futures
#
#\


def build_UT_with_friends (packet):
	driver_1 = packet ["driver_1"]
	driver_1_ICAN_DNS_Address = packet ["driver_1_ICAN_DNS_Address"]
	
	address_from = packet ["address_from"]
	address_to = packet ["address_to"]
	
	
	proceeds = {
		"unsigned_transaction_hexadecimal_string": ""
	}
	
	def goto_address ():
		driver_1.get (driver_1_ICAN_DNS_Address)
	
	
	outer_modal_buttons = {}
	def check_for_outer_modal_button ():
		outer_modal_buttons ["octas_gifts__version_1"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"[octas_gifts__version_1]"
		)
	
	
	#
	#	[address-chooser-td] [nets-choices]
	#
	#
	inner_modal_buttons = {}
	def check_for_inner_modal_buttons ():
		inner_modal_buttons ["next"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"button[modal-next]"
		)
		inner_modal_buttons ["back"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"button[modal-back]"
		)
	
	
	#
	#	field elements
	#
	#
	inputs = {}
	textareas = {}
	buttons = {}
	tds = {}
	selects = {}
	spans = {}
	def check_fields_existence ():
		selects ["nets-choices"] = Select (driver_1.find_element (By.CSS_SELECTOR, '[address-chooser-td] [nets-choices]'))
		spans ["icann_net_address"] = driver_1.find_element (By.CSS_SELECTOR, 'span[icann_net_address]')
		
		textareas ["icann_net_address"] = driver_1.find_element (By.CSS_SELECTOR, "[icann_net_address]")
		textareas ["from_aptos_address"] = driver_1.find_element (By.CSS_SELECTOR, "[from_aptos_address]")
		textareas ["to_aptos_address"] = driver_1.find_element (By.CSS_SELECTOR, "[to_aptos_address]")
		
		selects ["currency_chooser"] = driver_1.find_element (By.CSS_SELECTOR, "select[currency_chooser]")
		inputs ["amount"] = driver_1.find_element (By.CSS_SELECTOR, "input[amount]")
		inputs ["transaction_expiration"] = driver_1.find_element (By.CSS_SELECTOR, "[transaction_expiration]")
		
	
	#
	#	field choices
	#
	#
	def modify_fields ():
		selects ["nets-choices"].select_by_value ("devnet")
		
		textareas ["from_aptos_address"].clear ()
		textareas ["from_aptos_address"].send_keys (address_from)
		
		textareas ["to_aptos_address"].clear ()
		textareas ["to_aptos_address"].send_keys (address_to)
		
		inputs ["amount"].clear ()
		inputs ["amount"].send_keys (
			'0.01'
		)
		
		inputs ["transaction_expiration"].clear ()
		inputs ["transaction_expiration"].send_keys (
			'600'
		)
	
	def check_field_contents ():
		assert (
			spans ["icann_net_address"].text ==
			'https://api.devnet.aptoslabs.com/v1'
		)
		
		assert (
			len (textareas ["from_aptos_address"].get_attribute ('value')) >= 1
		)
		assert (
			len (textareas ["to_aptos_address"].get_attribute ('value')) >= 1
		)
		
	#
	#	unsigned_transaction_leaf
	#
	#
	UT_buttons = {}
	def check_unsigned_transaction_leaf ():
		UT_buttons ["transaction_as_object_button"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_leaf] [transaction_as_object_button]"
		)
		UT_buttons ["transaction_as_hexadecimal_string_button"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_leaf] [transaction_as_hexadecimal_string_button]"
		)
		UT_buttons ["transaction_as_barcode_button"] = driver_1.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_leaf] [transaction_as_barcode_button]"
		)
	
		
	
	
	#
	#	This checks for the hexadecimal string
	#
	#
	proceeds = {}
	def check_the_UT_hexadecimal_string ():
		boat = driver_1.find_element (
			By.CSS_SELECTOR, 
			"[health=UT_Object__UT_hexadecimal_string]"
		)
		
		assert (len (boat.text) >= 1);
		
		proceeds [ "unsigned_transaction_hexadecimal_string" ] = boat.text.strip ()
		
		
		
	goto_address ()
	
	#
	#	Check that can open modal, then open the modal
	#
	#
	loop (check_for_outer_modal_button)
	outer_modal_buttons ["octas_gifts__version_1"].click ()
	
	#
	#	Check the contents of the modal
	#
	#
	loop (check_for_inner_modal_buttons)
	loop (check_fields_existence)
	
	modify_fields ()
	
	loop (check_field_contents)
	inner_modal_buttons ["next"].click ()
	
	loop (check_unsigned_transaction_leaf)
	loop (lambda : check_UT_Object (driver_1));
	UT_buttons ["transaction_as_hexadecimal_string_button"].click ()
	
	loop (check_the_UT_hexadecimal_string)
	
	#time.sleep (10)
	
	
	return [
		proceeds ["unsigned_transaction_hexadecimal_string"],
		inner_modal_buttons
	]
	
	#