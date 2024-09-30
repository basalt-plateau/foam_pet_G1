

<script>

/*
	import Field from '$lib/trinkets/Field/Trinket.svelte'

	const field_on_change = () => {
		
	}
	
	<Field 
		logo="Max Gas Amount, in Octas"
		
		bind:this={ field }
		on_change={ field_on_change }		
	/>
	
	
	onMount (() => {
		field.modify_packet ("600")
	})
*/

/*
	grid-template-columns:
		repeat(auto-fit, minmax(200px, 1fr))
*/

import { onMount } from 'svelte'
import { has_field } from 'procedures/object/has_field'

import Problem_Alert from '$lib/trinkets/Alerts/Problem.svelte'

export let logo = ""
export let packet_type = "number"
export let on_change = () => {}

let problem_alert = "";

const is_bracket = (might) => {
	return might !== null && typeof might === 'object';
}

const verify_is_great = () => {
	const proceeds = on_change ({ packet })
	
	
	if (is_bracket (proceeds) && has_field (proceeds, "problem")) {
		if (proceeds.problem.length >= 1) {
			problem_alert = proceeds.problem
			return;
		}
	}
	
	problem_alert = ""
}

export const modify_packet = (fresh_packet) => {
	packet = fresh_packet;
}

//
//
let packet = ""
$: {
	let _packet = packet;
	verify_is_great ()
}
//
//

function typeAction(node) {
	node.type = packet_type;
}



</script>



<div 
	class="card variant-soft-primary p-1" 
	style="
		color: inherit
	"
>	
	<div
		style="
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
			grid-template-rows: auto;
			gap: 0.1cm;
			
			color: inherit
		"
	>
		<span 
			class="badge variant-soft-primary"
			style="
				word-wrap: revert-layer;
				white-space: preserve;
			"
		>{ logo }</span>
		
		<label 
			class="label"
			style="display: flex; align-items: center;"
		>
			<input 
				monitor="field"
			
				bind:value={ packet }
				use:typeAction
				
				on:keyup={ verify_is_great }
				
				class="input"
				style="
					text-indent: 10px; 
					padding: 0.1cm;
					padding-right: 0.3cm;
				" 
				
				placeholder="" 
			/>
		</label>
	</div>
	<div>
		{#if problem_alert.length >= 1 }
		<div style="height: 8px"></div>
		
		<Problem_Alert 
			size="small"
		
			text={ problem_alert }
		/>
		{/if}
	</div>
</div>