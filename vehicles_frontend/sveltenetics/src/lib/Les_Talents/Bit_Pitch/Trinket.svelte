











<script>

/*
	import Bit_Pitch from '$lib/Les_Talents/Bit_Pitch/Trinket.svelte'
	import { open_bit_throw } from '$lib/Les_Talents/Bit_Pitch/open.js'
*/


//
//
import { RadioGroup, RadioItem } from '@skeletonlabs/skeleton';
import _merge from 'lodash/merge'
//
//
import Polytope from '$lib/trinkets/Polytope/Fabric.svelte'
import Barcode_Visual from '$lib/trinkets/Barcode/Visual/Trinket.svelte'
import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'
import Barcode_Vision from '$lib/trinkets/Barcode/Vision/Trinket.svelte'
//
//
import Alert_Success from '$lib/trinkets/Alerts/Success.svelte'
	


let barcode_vision = ""
const on_barcode_found = async ({ hexadecimal_string }) => {
	console.info ({ hexadecimal_string });
	
	barcode_vision.stop_the_scan ();
}
	

let bits = ""
let direction = "send"

const prepare = () => {
	return {
		name: "Transfer",
		next: "yes",
		back: "yes"
	}
}

let polytope_modal;

const on_click = () => {
	polytope_modal.advance (({ freight }) => {
		freight.name = "panel"
		return freight;
	})
}

const on_modal_change = () => {}

let current = 1;
const on_next_pressed = () => {
	console.info ("on_next_pressed")
	
	polytope_modal.advance (({ freight }) => {
		
		if (freight.panel_name === "Send Bits") {
			current += 1
			
			freight.panel_name = "Send Bits, QR Code"
			freight.next.permitted = "no"
			freight.back.permitted = "yes"
		}
		else if (freight.panel_name === "Send Bits, QR Code") {
			
			
		}
		

		
		return freight;		
	})
}
const on_back_pressed = () => {
	console.info ("on_back_pressed")
	
	polytope_modal.advance (({ freight }) => {
		if (freight.panel_name === "Send Bits, QR Code") {
			current -= 1
			
			freight.panel_name = "Send Bits"
			freight.next.permitted = "yes"
			freight.back.permitted = "no"
		}
		

		
		return freight;		
	})
}

const on_prepare = () => {
	polytope_modal.advance (({ freight }) => {
		return _merge ({}, freight, {
			showing: 'yes',
			name: 'Bit Pitch',
			
			
			panel_name: 'Send Bits',
			
			unfinished: {
				showing: 'no',
			},
			
			
			back: {
				text: 'Back',
				permitted: "yes",
				go: () => {
					console.log ('back pressed')
					on_back_pressed ()
				}
			},
			next: {
				//
				//	{ text: "Unfinished", permitted: "no" }
				//
				text: 'Next',
				permitted: "yes",
				has_alert: "yes",
				go: () => {
					on_next_pressed ()
				}
			},
			panel: {
				text: ''
			}
		})
		
		// freight.name = "panel"
		// freight.show = "yes"
		return freight;
	})
}

</script>


<Polytope 
	bind:this={ polytope_modal }
	on_change={ on_modal_change }
	on_prepare={ on_prepare }
>
	
	<div 
		slot="leaves"
		style="
				height: 100%;
				width: 100%;
				
				display: flex;
				// justify-content: center;
				align-items: center;
				
				flex-direction: column;
				
				max-width: 25cm;
				
				margin: 0 auto;
			"
	>
		<div style="height: 1cm" />
	
		<p>Bits can be sent and received from here.</p>

		<div style="height: 1cm" />

		<RadioGroup>
			<RadioItem bind:group={ direction } name="justify" value={ "send" }>Send</RadioItem>
			<RadioItem bind:group={ direction } name="justify" value={ "receive" }>Receive</RadioItem>
		</RadioGroup>
		
		{#if direction === "send" }
		{#if current === 1 }
		<div 
			style="
				width: 100%;
				margin: 1em;
			"
			class="card p-4"
		>
			<p
				style="
					text-align: center;
					padding: 0.5cm;
				"
			>After entering bits, the "Next" button forms a barcode.</p>
		
			<label 
				style="
					
					width: 100%;
				"
				class="label"
			>
				<textarea 
					bind:value={ bits }
				
					style="
						padding: 1em;
						width: 100%;
					"
					class="textarea" 
					rows="4" 
					placeholder="" 
				/>
			</label>
		</div>
		{:else if current === 2}
		<label 
			style="
				padding: 1em;
				width: 100%;
			"
			class="label"
		>
			<Barcode_Visual 
				hexadecimal_string={ bits }
			/>
		</label>
		{/if}
		{:else}
		<div
			style="
				height: 100%;
				width: 100%;
				padding-top: 1cm;
			"
		>
			<Barcode_Vision
				bind:this={ barcode_vision }
				found={ on_barcode_found }
				
				styles={{
					'height': '100%',
					'width': '100%',
					'max-width': '1000px'
				}}
			/>
		</div>
		{/if}
	</div>
	
	
	<div slot="unfinished">
		<div>
			This is unfinished
		</div>
	</div>
</Polytope>