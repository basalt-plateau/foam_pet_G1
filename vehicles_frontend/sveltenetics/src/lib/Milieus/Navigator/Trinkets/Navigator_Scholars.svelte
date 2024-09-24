

<script>

import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'

import { onMount, onDestroy } from 'svelte'
import { check_Milieus_truck, monitor_Milieus_truck } from '$lib/Milieus/Truck'

let mode;
let location = [ "", "" ];

let update_variables = () => {
	mode = check_Milieus_truck ().freight.mode;
	location = check_Milieus_truck ().freight.location;
}
update_variables ();


let Scholars_Trucks_Prepared = "no"
let Scholars_Trucks_Monitor;
let Scholars_Trucks_Freight;
onMount (async () => {
	Scholars_Trucks_Freight = check_Milieus_truck ().freight; 
	
	Scholars_Trucks_Monitor = monitor_Milieus_truck ((_freight) => {
		Scholars_Trucks_Freight = _freight;
		
		// mode = Scholars_Trucks_Freight.mode;
		// location = Scholars_Trucks_Freight.location;
		
		update_variables ();
	})
	
	update_variables ();
	
	Scholars_Trucks_Prepared = "yes"
});

onDestroy (() => {
	Scholars_Trucks_Monitor.stop ()
}); 

</script>


<div>
	{#if location [0] === "Scholars" }
	<div>
		<Milieus_Button
			name={ "Hints" }
			location={[ "Scholars", "Hints" ]}
			is_open_location={[ "Scholars", "Hints" ]}
		/>
		<Milieus_Button
			name={ "Wild" }
			location={[ "Scholars", "Wild" ]}
			is_open_location={[ "Scholars", "Wild" ]}
		/>
		<Milieus_Button
			name={ "Theme" }
			location={[ "Scholars", "Theme" ]}
			is_open_location={[ "Scholars", "Theme" ]}
		/>
	</div>
	{/if}
</div>