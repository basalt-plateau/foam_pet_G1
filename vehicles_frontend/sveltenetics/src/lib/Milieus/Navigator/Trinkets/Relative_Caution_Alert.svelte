



<script>


/*
	If Relatives and Can Connect, say "Caution, Internet connection established.
	The "Relatives" activities
	should happen on a trinket that isn't connected
	to the internet."
*/

////
//
import { onMount, onDestroy } from 'svelte'
//
//
import { check_roomies_truck, monitor_roomies_truck } from '$lib/Versies/Trucks'
import Slang from '$lib/trinkets/Slang/Trinket.svelte'
import Problem_Alert from '$lib/trinkets/Alerts/Problem.svelte'
import Caution_Alert from '$lib/trinkets/Alerts/Caution.svelte'
//
////

import Milieus_Truck from '$lib/Milieus/Truck/Trinket.svelte'
import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'

	


let is_relatives_location = "no"

let Milieus_freight = {}
let Milieus_trucks_prepared = "no"
const on_Milieus_truck_change = ({ freight: _freight, happening }) => {
	Milieus_freight = _freight;
	if (happening === "mounted") {
		Milieus_trucks_prepared = "yes"
	}
	
	console.log ({ _freight })
	
	try {
		if (_freight.location [0] === "Relatives") {
			is_relatives_location = "yes"
			return;
		}
	}
	catch (exception) {};

	is_relatives_location = "no"
}



let net_connected = "no"

let RT_Prepared = "no"
let RT_Monitor;
let RT_Freight;
onMount (async () => {
	const Truck = check_roomies_truck ()
	RT_Freight = Truck.freight; 
	net_connected = RT_Freight.net_connected;
	
	RT_Monitor = monitor_roomies_truck ((_freight) => {
		RT_Freight = _freight;
		net_connected = _freight.net_connected;
		
		console.log ({ net_connected })
	})
	
	
	RT_Prepared = "yes"
});

onDestroy (() => {
	RT_Monitor.stop ()
}); 


</script>


<div>
	<Milieus_Truck on_change={ on_Milieus_truck_change }/>
	
	{#if (
		Milieus_trucks_prepared === "yes" && 
		RT_Prepared === "yes" &&
		net_connected === "yes" &&
		is_relatives_location === "yes"
	)} 
	<div
		style="
			padding: 0 20px;
			max-width: 28cm;
			margin: 0 auto;
		"
	>
		<Problem_Alert show="yes">	
			<div 
				style="line-height: 2em;"
				class="card p-2 variant-filled-warning"
			>
				
				<p style="line-height: inherit;"><b>Caution!</b> A connection to an <Slang text="Internet_Location" /> was established.</p>
				<p style="line-height: inherit;">These <b>Relatives</b> activities should happen on a <Slang text="Machine" /> that has limited connectivity.</p>
				<p style="line-height: inherit;">
					<span>A <Slang text="Label" /> for <Slang text="an_Offline_Machine" /> can be adopted from </span>
					<Milieus_Button
						name={ "Wild" }
						location={[ "Scholars", "Wild" ]}
						is_open_location={[ "Scholars" ]}
					/>
				</p>
			</div>
		</Problem_Alert>
	</div>
	{/if}
</div>
