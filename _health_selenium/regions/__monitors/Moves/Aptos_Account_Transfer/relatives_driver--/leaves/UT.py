



#/
#
from vivaciousness.procedures.loop import loop
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




def UT_leaf (packet):
	driver_2 = packet ["driver_2"]
	inner_modal_buttons = packet ["inner_modal_buttons"]

	buttons = {}
	def check_field ():
		buttons ["UT_hexadecimal_string_button"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[longevity=UT_hexadecimal_string_button]"
		)
		buttons ["UT_object_button"] = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[longevity=UT_object_button]"
		)

	#/
	#	This checks for the hexadecimal string
	#		unsigned_transaction_fiberized
	#
	def check_the_UT_hexadecimal_string ():
		boat = driver_2.find_element (
			By.CSS_SELECTOR, 
			"[unsigned_transaction_hexadecimal_string]"
		)
		UT_hexadecimal_string = boat.text.strip ()
		assert (len (UT_hexadecimal_string) >= 10);
	#
	#\
	
	loop (check_field)
	buttons ["UT_hexadecimal_string_button"].click ()
	
	loop (check_the_UT_hexadecimal_string)
	inner_modal_buttons ["next"].click ()