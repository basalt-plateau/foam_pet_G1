




def monitor_health (packet):
	glob_string = packet ["glob_string"]
	vehicles = packet ["vehicles"]
	this_vehicle = packet ["this_vehicle"]
	db_directory = packet ["db_directory"]
	

	promote = Emergency.on ({
		"glob_string": glob_string,
		
		"simultaneous": True,
		"simultaneous_capacity": 50,

		"time_limit": 60,

		"module_paths": [
			vehicles
		],

		"relative_path": this_vehicle,
		
		"db_directory": db_directory,
		
		"aggregation_format": 2
	})


	promote ["off"] ()



	#
	#	This is a detailed report
	#	of the technique.
	#
	rich.print_json (data = {
		"paths": promote ["proceeds"] ["paths"]
	})

	#
	#	This is the checks that did 
	#	not finish successfully.
	#
	rich.print_json (data = {
		"alarms": promote ["proceeds"] ["alarms"]
	})

	#
	#	This is concise stats about
	#	the  technique.
	#
	rich.print_json (data = {
		"stats": promote ["proceeds"] ["stats"]
	})