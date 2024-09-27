

<script>
import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'


import { onMount, onDestroy } from 'svelte'
import { check_roomies_truck, monitor_roomies_truck } from '$lib/Versies/Trucks'
	
import Relatives from '$lib/Letters/Relatives.svelte'

import { parse_styles } from '$lib/trinkets/styles/parse'
	
	
let mode = check_roomies_truck ().freight.mode;
let window_width = check_roomies_truck ().freight.window_width;

let Scholars_Trucks_Prepared = "no"
let Scholars_Trucks_Monitor;
let Scholars_Trucks_Freight;
onMount (async () => {
	const Truck = check_roomies_truck ()
	Scholars_Trucks_Freight = Truck.freight; 
	
	Scholars_Trucks_Monitor = monitor_roomies_truck ((_freight) => {
		Scholars_Trucks_Freight = _freight;
		build ()
	})
	
	build ();
	
	Scholars_Trucks_Prepared = "yes"
});

onDestroy (() => {
	Scholars_Trucks_Monitor.stop ()
}); 



let buttons_styles = ""
const build = () => {
	mode = check_roomies_truck ().freight.mode;
	window_width = check_roomies_truck ().freight.window_width;
	
	console.log ("build", window_width)
	
	if (window_width > 800) {
		buttons_styles = 'padding: 0.3cm 0.7cm; margin: 0 0.1cm; font-size: 1.2em'
	}
	else {
		buttons_styles = ''
	}
}

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

// "ᎤᏓᏅᏙᏗ"
let relatives_name = (
	"ᐊᔭᖅ"
)

let relatives_name_2 = '/pictures/relatives.svg';

/*
	<img 
		style="
			height: 1.4cm;
		"
		src={ pet } 
		alt="pet" 
	/>
*/

</script>


<div
	style="
		display: flex;
		gap: 0.2cm;
		
		font-size: 1.3em;
	"
>
	<Milieus_Button
		monitor="Scholars"
		
		name={ seeds_name }
		location={[ "Scholars", "Hints" ]}
		is_open_location={[ "Scholars" ]}
		
		style={ buttons_styles }
	/>
	<Milieus_Button
		monitor="Friends"
	
		name={ friends_name }
		location={[ "Friends", "Vacations" ]}
		is_open_location={[ "Friends" ]}
		
		style={ buttons_styles }
	/>
	
	<Milieus_Button
		monitor="Relatives"
	
		location={[ "Relatives", "Hints" ]}
		is_open_location={[ "Relatives" ]}
		
		component={ Relatives }
		component_props={{
			style: {
				width: '100px'
			}
		}}
		
		style={ buttons_styles }
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