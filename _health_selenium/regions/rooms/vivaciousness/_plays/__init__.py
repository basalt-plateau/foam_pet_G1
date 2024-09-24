
'''
from vivaciousness._plays import retrieve_plays
plays = retrieve_plays ();
'''



def retrieve_plays ():
	URL = "https://localhost"
	URL = "http://localhost:21000"
	URL = "http://localhost:22000"
	#URL = "https://45.77.86.6"

	open_browser = "yes"
	open_browser = "yes"
	

	return {
		#
		#	whether to show the browser, "yes"
		#	or not show the browser, "no"
		#
		"open browser": open_browser,
		
		"URL": URL,
		
		"accounts": {
			"1": {
				"private key": "89ABC8DE9FABDE0716253407612534071562348F9AEDBC8F9EADBC0127653425",
				"address": "522D906C609A3D23B90F072AD0DC74BF857FB002E211B852CE38AD6761D4C8FD"
			},
			"2": {
				"private key": "BF84073526170CB5AE94370DAE9F8437052E1CBF8E9CA52F0486B7052E9CB705",
				"address": "26F4F8D7C5526BA7DA453041D3A858CFEA06D911C90C2E40EDA2A7261826858C"
			}
		}
	}