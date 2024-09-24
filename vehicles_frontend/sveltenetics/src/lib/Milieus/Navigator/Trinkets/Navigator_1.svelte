

<script>
import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'


import { onMount, onDestroy } from 'svelte'
import { check_Milieus_truck, monitor_Milieus_truck } from '$lib/Milieus/Truck'
import { check_roomies_truck } from '$lib/Versies/Trucks'
	
let mode = check_roomies_truck ().freight.mode;

let Scholars_Trucks_Prepared = "no"
let Scholars_Trucks_Monitor;
let Scholars_Trucks_Freight;
onMount (async () => {
	const Truck = check_Milieus_truck ()
	Scholars_Trucks_Freight = Truck.freight; 
	
	Scholars_Trucks_Monitor = monitor_Milieus_truck ((_freight) => {
		Scholars_Trucks_Freight = _freight;
		
		mode = check_roomies_truck ().freight.mode;
	})
	
	Scholars_Trucks_Prepared = "yes"
});

onDestroy (() => {
	Scholars_Trucks_Monitor.stop ()
}); 


/*
let seeds_name = (
	"পণ্ডিত"
)
*/

let seeds_name = (
	"அறிஞர்கள்"
)
let friends_name = (
	"ጓደኛዎች"
)
let relatives_name = (
	"ᎤᏓᏅᏙᏗ"
)

</script>


<div
	style="
		display: flex;
		gap: 0.2cm;
	"
>
	<Milieus_Button
		monitor="Scholars"
		
		name={ seeds_name }
		location={[ "Scholars", "Hints" ]}
		is_open_location={[ "Scholars" ]}
	/>
	<Milieus_Button
		monitor="Friends"
	
		name={ friends_name }
		location={[ "Friends", "Vacations" ]}
		is_open_location={[ "Friends" ]}
	/>
	<Milieus_Button
		monitor="Relatives"
	
		name={ relatives_name }
		location={[ "Relatives", "Hints" ]}
		is_open_location={[ "Relatives" ]}
	/>
	
	
	{#if mode === "nurture" }
	<!-- <div style="width: 0.5cm"></div> -->
	<!-- <The_Map_Trinket /> -->
	

	<Milieus_Button
		name={ "Technicians" }
		location={[ "Technicians", "Map" ]}
		is_open_location={[ "Technicians" ]}
	/>
	{/if}
</div>