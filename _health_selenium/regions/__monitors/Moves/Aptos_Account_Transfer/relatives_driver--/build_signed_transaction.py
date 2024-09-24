

#/
#
from vivaciousness.health_regions.connect import connect_to_driver
from vivaciousness.procedures.Faucet.Give import give_Octas_from_faucet
#
from .leaves.UTS import UTS_leaf
from .leaves.UT import UT_leaf
from .leaves.ST import ST_leaf
#
#
from selenium.webdriver.common.by import By
#
#
import traceback
import json
import time
import multiprocessing
import concurrent.futures
#
#\

from vivaciousness.procedures.loop import loop


def build_ST_with_relatives (packet):
	driver_2 = packet ["driver_2"]
	driver_2_ICAN_DNS_Address = packet ["driver_2_ICAN_DNS_Address"]
	unsigned_transaction_hexadecimal_string = packet ["unsigned_transaction_hexadecimal_string"]
	account_1 = packet ["account_1"]
	
	assert (
		len (unsigned_transaction_hexadecimal_string) >= 1
	), unsigned_transaction_hexadecimal_string

	def goto_address ():
		driver_2.get (driver_2_ICAN_DNS_Address)
		
	# [unsigned_transaction_fields_leaf] [barcode_camera_button]
	# [unsigned_transaction_fields_leaf] [hexadecimal_field_button]
	
	# [consider_a_transaction]
	outer_modal_buttons = {}
	def check_for_modal_opener ():
		outer_modal_buttons ["consider_a_transaction"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[consider_a_transaction]"
		)
	
	
	#
	#	[address-chooser-td] [nets-choices]
	#
	#
	inner_modal_buttons = {}
	def check_for_inner_modal_buttons ():
		inner_modal_buttons ["next"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"button[modal-next]"
		)
		inner_modal_buttons ["back"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"button[modal-back]"
		)
	
	#
	#	unsigned_transaction_leaf
	#
	#
	UT_buttons = {}
	def check_unsigned_transaction_leaf ():
		UT_buttons ["barcode_camera_button"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_fields_leaf] [barcode_camera_button]"
		)
		UT_buttons ["hexadecimal_field_button"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_fields_leaf] [hexadecimal_field_button]"
		)
		
	textareas = {}
	UT_hexadecimal_fields_buttons = {}
	def check_unsigned_transaction_hexadecimal_field ():
		textareas ["UT_hexadecimal_string"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_fields_leaf] textarea[UT_hexadecimal_string]"
		)
		UT_hexadecimal_fields_buttons ["UT_hexadecimal_string_add_button"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"button[UT_hexadecimal_string_add_button]"
		)
		
		
	def add_UT_to_UT_field_textarea ():
		textareas ["UT_hexadecimal_string"].clear ()
		textareas ["UT_hexadecimal_string"].send_keys (unsigned_transaction_hexadecimal_string)
		
		
	def check_UT_field_textarea ():
		assert (
			len (textareas ["UT_hexadecimal_string"].get_attribute ('value')) >= 1
		)
	
	
	
		
	
	
	
	goto_address ();		
		
	#/
	#	open the modal
	#
	#
	loop (check_for_modal_opener)
	outer_modal_buttons ["consider_a_transaction"].click ()
	loop (check_for_inner_modal_buttons)
	#
	#\
	
	#/
	#	unsigned transaction fields leaf
	#
	#
	loop (check_unsigned_transaction_leaf)
	UT_buttons ["hexadecimal_field_button"].click ()
	loop (check_unsigned_transaction_hexadecimal_field)
	#
	add_UT_to_UT_field_textarea ()
	loop (check_UT_field_textarea)
	UT_hexadecimal_fields_buttons ["UT_hexadecimal_string_add_button"].click ()
	#
	inner_modal_buttons ["next"].click ()
	#
	#\
	
	#/
	#	unsigned transaction leaf
	#
	#
	UT_leaf ({
		"driver_2": driver_2,
		"inner_modal_buttons": inner_modal_buttons
	})
	#
	#\
	
	#/
	#	unsigned transaction signature leaf
	#
	#
	UTS_leaf ({
		"driver_2": driver_2,
		"inner_modal_buttons": inner_modal_buttons,
		"account_1": account_1
	})
	#
	#\
	
	#/
	#	signed transaction leaf
	#
	#
	[ signature_hexadecimal_string ] = ST_leaf ({
		"driver_2": driver_2,
		"inner_modal_buttons": inner_modal_buttons
	})
	#
	#\
	
	print (f"""
	
	
	
		[signature_hexadecimal_string___]: { signature_hexadecimal_string }
	
	
	
	
	""")

	return [ signature_hexadecimal_string ]

