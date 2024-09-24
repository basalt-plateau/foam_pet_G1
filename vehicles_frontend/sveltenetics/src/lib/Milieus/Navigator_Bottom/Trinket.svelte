



<script>

///
//
// https://lucide.dev/guide/packages/lucide-svelte#one-generic-icon-component
// https://lucide.dev/icons/
//
//

//\\
//
//
import Milieus_Truck from '$lib/Milieus/Truck/Trinket.svelte'
import { check_roomies_truck } from '$lib/Versies/Trucks'
//
////

let mode = check_roomies_truck ().freight.mode;


let navigator_1;

let seeds_freight = {}
let seeds_trucks_prepared = "no"
const on_seeds_truck_change = ({ freight: _freight, happening }) => {
	seeds_freight = _freight;
	if (happening === "mounted") {
		seeds_trucks_prepared = "yes"
	}
}



</script>

{#if mode === "nurture" }
<nav>
	<Milieus_Truck on_change={ on_seeds_truck_change }/>
		
	<hr class="!border-t-2" />
	<div class="bg-surface-100-800-token w-full"
		style="
			padding: 0 2px;
		"
	>
		<p>{ seeds_freight.location }</p>
	</div>
</nav>
{/if}