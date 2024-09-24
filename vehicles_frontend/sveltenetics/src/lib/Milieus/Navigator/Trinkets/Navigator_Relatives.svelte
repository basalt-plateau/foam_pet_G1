

<script>

import Signatures_Component from './Navigator_Relatives/Signatures.svelte'


import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'

import { onMount, onDestroy } from 'svelte'
import { check_Milieus_truck, monitor_Milieus_truck } from '$lib/Milieus/Truck'

let mode = check_Milieus_truck ().freight.mode;
let location = check_Milieus_truck ().freight.location;

let Scholars_Trucks_Prepared = "no"
let Scholars_Trucks_Monitor;
let Scholars_Trucks_Freight;
onMount (async () => {
	Scholars_Trucks_Freight = check_Milieus_truck ().freight; 
	
	Scholars_Trucks_Monitor = monitor_Milieus_truck ((_freight) => {
		Scholars_Trucks_Freight = _freight;
		
		mode = Scholars_Trucks_Freight.mode;
		location = Scholars_Trucks_Freight.location;
	})
	
	Scholars_Trucks_Prepared = "yes"
});

onDestroy (() => {
	Scholars_Trucks_Monitor.stop ()
}); 

</script>


{#if location [0] === "Relatives" }
<div
	style="
		display: flex;
		gap: 0.2cm;
	"
>
	<Milieus_Button
		name={ "Hints" }
		location={[ "Relatives", "Hints" ]}
		is_open_location={[ "Relatives", "Hints" ]}
	/>
	<Milieus_Button
		name={ "Accounts" }
		location={[ "Relatives", "Accounts" ]}
		is_open_location={[ "Relatives", "Accounts" ]}
	/>
	<Milieus_Button
		name={ "Signatures" }
		location={[ "Relatives", "Signatures" ]}
		is_open_location={[ "Relatives", "Signatures" ]}
		component={ Signatures_Component }
	/>
</div>
{/if}

