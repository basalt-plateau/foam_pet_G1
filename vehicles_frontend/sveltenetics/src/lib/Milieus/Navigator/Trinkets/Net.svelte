
<script>

import { onMount, onDestroy } from 'svelte'

import {
	check_roomies_truck,
	monitor_roomies_truck
} from '$lib/Versies/Trucks'


let RT_Prepared = "no"
let RT_Monitor;
let RT_Freight;
onMount (async () => {
	const Truck = check_roomies_truck ()
	RT_Freight = Truck.freight; 
	
	RT_Monitor = monitor_roomies_truck ((_freight) => {
		RT_Freight = _freight;
	})
	
	RT_Prepared = "yes"
});

onDestroy (() => {
	RT_Monitor.stop ()
}); 

</script>

{#if RT_Prepared === "yes" }
<div
	style="
		display: flex;
		justify-content: center;
		align-items: center;
	"
>
	<aside 
		style="
			padding: 4px 8px;
			margin: 8px 0;
			display: inline-block;
			min-width: 300px;
		"
	>
        <div 
			class="badge variant-soft"
			style="
					position: relative;
					font-size: 1em;
				"
		>
			<span>net</span>
			
			<span style="width: 0.1cm"></span>
			
			<span
				class="badge variant-filled-surface"
				style="
					margin: 0;
				"
			>{ RT_Freight.net_name }</span>
			
			<span style="width: 0.1cm"></span>
			
			<span
				class="badge variant-filled-surface"
				style="
					margin: 0;
				"
			>{ RT_Freight.net_path }</span>
        </div>
    </aside>
</div>
{/if}