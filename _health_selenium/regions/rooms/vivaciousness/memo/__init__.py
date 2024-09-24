
''''
from vivaciousness.memo import proceed_through_memo
proceed_through_memo ({ "driver": driver });
"'''


from vivaciousness.procedures.loop import loop
from selenium.webdriver.common.by import By

def proceed_through_memo (packet):
	driver = packet ["driver"]
		
	def check_fields_existence ():
		return driver.find_element (
			By.CSS_SELECTOR, 
			"[monitor='memo'] [monitor='proceed button']"
		)
		
		
	button = loop (check_fields_existence)
	button.click ();
		
		
		
		
		
		