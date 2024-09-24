



<script>

import Problem_Alert from '$lib/trinkets/Alerts/Problem.svelte'
import Caution_Alert from '$lib/trinkets/Alerts/Caution.svelte'

/*
If Relatives and Can Connect, say "Caution, Internet connection established.
The "Relatives" activities
should happen on a trinket that isn't connected
to the internet."
*/

import { onMount, onDestroy } from 'svelte'
import { check_roomies_truck, monitor_roomies_truck } from '$lib/Versies/Trucks'
import Slang from '$lib/trinkets/Slang/Trinket.svelte'
	
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

// RT_Freight.net_path
// RT_Freight.net_name

</script>


{#if RT_Prepared === "yes" && net_connected === "yes" }
<div
	style="
		padding: 0 20px;
		max-width: 28cm;
		margin: 0 auto;
	"
>
	<Problem_Alert show="yes">	
		<div class="card p-2 variant-filled-warning" style="">
			<p><b>Caution!</b> A connection to an <Slang text="Internet_Location" /> was established.</p>
			<p>These <b>Relatives</b> activities should happen on a <Slang text="Machine" /> that has limited connectivity.</p>
		</div>
	</Problem_Alert>
</div>
{/if}