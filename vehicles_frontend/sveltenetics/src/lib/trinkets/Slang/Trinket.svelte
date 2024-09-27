

<script>

/*
	import Slang from '$lib/trinkets/Slang/Trinket.svelte'
	<Slang text="transaction" />
*/

/*
	Currently supports replacing 1 or 2 word sayings.
*/

/*
	@ Legend
		@ Vernacular
		@ Jargon
*/

/*
	Decipher Aristocratic English into Regular English.
*/

////
//
import { has_field } from 'procedures/object/has_field'
import { onMount, onDestroy } from 'svelte'
import nlp from 'compromise/one'
//
//
import { check_roomies_truck, monitor_roomies_truck } from '$lib/Versies/Trucks'
//
//
import { nocturnalize } from './screenplays/nocturnalize'
import { English_1 } from './jargons/English_1'
//
////

const language = "English"
const legend = {
	"Chinese": {},
	"Francais": {},
	"Spanish": {},
	
	"English": English_1,
}

// let legendary = legend [ language ] [ text ]
let legend_language = legend [ language ]

var built = []

////
//
export let style = ""
export let text = ""
$: {
	let _text = text;
	build ();
}
//
////


let use_slang;
const build = () => {
	try {
		if (Seeds_Trucks_Freight && has_field (Seeds_Trucks_Freight, "use_slang")) {
			if (use_slang !== Seeds_Trucks_Freight.use_slang) {
				use_slang = Seeds_Trucks_Freight.use_slang;
				
				if (use_slang === "yes") {
					built = nocturnalize ({ legend_language, text })
				}
				else {
					built = nocturnalize ({ legend_language, text, slang: "no" })
				}
			}
		}
	}
	catch (exception) {
		console.error (exception)
	}
}


let Seeds_Trucks_Prepared = "no"
let Seeds_Trucks_Monitor;
let Seeds_Trucks_Freight;
onMount (async () => {
	const Truck = check_roomies_truck ()
	Seeds_Trucks_Freight = Truck.freight; 
	
	Seeds_Trucks_Monitor = monitor_roomies_truck ((_freight) => {
		Seeds_Trucks_Freight = _freight;
		
		if (use_slang !== Seeds_Trucks_Freight.use_slang) {
			build ()
		}	
	})
	
	build ()
	
	Seeds_Trucks_Prepared = "yes"
});

onDestroy (() => {
	Seeds_Trucks_Monitor.stop ()
}); 


let actual_styles = `
	color: inherit;
			
	font-weight: bold;
	font-size: 1em;
	
	white-space: break-spaces;
` + style;

</script>




<span>
	{#each built as part }
	{#if part.code === "yes"}
		<span><code
			class="code"
			style={ actual_styles }
		>{ part.text }</code></span>
	{:else}
		<span>{ part.text }</span>
	{/if}
	{/each}
</span>
