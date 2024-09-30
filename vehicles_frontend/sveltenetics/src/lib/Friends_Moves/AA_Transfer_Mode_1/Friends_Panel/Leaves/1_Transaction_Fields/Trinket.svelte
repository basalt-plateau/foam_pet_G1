



<script>


////
///
//
import * as AptosSDK from "@aptos-labs/ts-sdk";
//
import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';
import { Modal, getModalStore } from '@skeletonlabs/skeleton';
import { getToastStore } from '@skeletonlabs/skeleton';
import { onMount, onDestroy } from 'svelte';
//
//
import { parse_styles } from '$lib/trinkets/styles/parse.js';
import Panel from '$lib/trinkets/panel/trinket.svelte'
import Net_Choices from '$lib/PTO/Nets/Choices.svelte'
//
import Amount_Field from '$lib/trinkets/Amount_Field/Trinket.svelte'
import Address_Qualities_Trinket from '$lib/trinkets/Address_Qualities/Trinket.svelte'
//
import { 
	retrieve_truck, 
	monitor_truck,
} from '$lib/Friends_Moves/AA_Transfer_Mode_1/Friends_Panel/Logistics/Truck'
//
import { assert_is_natural_numeral_string } from '$lib/taverns/numerals/natural/is_string'
//
//\
//\\
import { ask_for_freight } from '$lib/Versies/Trucks'
import Field from '$lib/trinkets/Field/Trinket.svelte'


////
//
//	Max Gas Amount
//
//
let max_gas_amount_field = ""
const max_gas_amount_on_change = ({ packet }) => {
	const actual_packet_type = typeof packet;
	
	try {
		assert_is_natural_numeral_string (packet)
	}
	catch (exception) {
		return {
			"problem": exception.message
		}
	}
	
	freight.fields.max_gas_amount = packet
	
	return {}
}
const max_gas_amount_on_prepare = () => {
	max_gas_amount_field.modify_packet ("200000")
}
//
////





let prepared = "no"
let Truck_Monitor;
let freight;
onMount (() => {
	const Truck = retrieve_truck ()
	freight = Truck.freight; 
	
	//
	//
	//
	//
	freight.current.land = "Transaction_Fields"

	Truck_Monitor = monitor_truck ((freight) => {
		console.log ("Transaction Fields: Truck_Monitor", { freight })
	})
	
	const roomies_freight = ask_for_freight ();
	freight.fields.ICANN_net_path = roomies_freight.net_path;
	freight.fields.net_name = roomies_freight.net_name;
	
	prepared = "yes"
});
onDestroy (() => {
	Truck_Monitor.stop ()
});

const on_amount_change = ({ 
	effects,
	actual_amount_of_Octas
}) => {
	console.log ("on_amount_change", actual_amount_of_Octas)
	
	if (effects.problem === "") {
		freight.fields.actual_amount_of_Octas = actual_amount_of_Octas;
	}
}


let origin_address_trinket = ""
const on_prepare_origin_address = () => {
	origin_address_trinket.change_address_hexadecimal_string (
		freight.fields.from_address_hexadecimal_string
	)
}
const on_change_origin_address = ({
	effective,
	address_hexadecimal_string,
	exception
}) => {
	freight.fields.from_address_permitted = effective;
	freight.fields.from_address_exception = exception;
	freight.fields.from_address_hexadecimal_string = address_hexadecimal_string;
}


let to_address_trinket = ""
const on_prepare_to_address = () => {
	to_address_trinket.change_address_hexadecimal_string (
		freight.fields.to_address_hexadecimal_string
	)
}
const on_change_to_address = ({
	effective,
	address_hexadecimal_string,
	exception
}) => {
	freight.fields.to_address = effective;
	freight.fields.to_address = exception;
	freight.fields.to_address_hexadecimal_string = address_hexadecimal_string;
}


const link = "https://explorer.aptoslabs.com/account/0x0000000000000000000000000000000000000000000000000000000000000001/modules/run/aptos_account/transfer"

</script>


<style>

td {
	display: flex;
	flex-direction: column;
}

p {
	white-space: normal;
}

</style>

{#if prepared === "yes"}
<div transaction_petition_fields>
	<div class="card p-4">
		<header
			style="
				text-align: center;
				font-size: 2em;
			"
		>Petition Form</header>
	</div>
	
	<hr class="!border-t8" 
		style="
			border-style: dotted;
			border-top-width: 0.2cm;
			margin: 0.5cm 0;
		" 
	/>
	
	<div class="card p-2">
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<header
						style="
							text-align: center;
							font-size: 1.5em;
							padding: 0cm 0;
						"
					>Hints</header>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div>
						<p
							style="text-align: center; font-size: 1em"
						>This is for transfering APT from one address to another address.</p>
						
						<div class="card p-2"
							style="margin: .25cm 0"
						>
							<a 
								href={ link }
								target="_blank"
								style="
									word-break: break-all;
								"
							>{ link }</a>
						</div>
						
						<p>The procedure is:</p>
						<ol class="list">
							<li>
								<span class="badge p-2 variant-soft-primary">1. online</span>
								<span class="flex-auto">Generate the petition</span>
							</li>
							<li>
								<span class="badge p-2 variant-soft-tertiary">2. offline</span>
								<span class="flex-auto">Scan the petition QR code</span>
							</li>
							<li>
								<span class="badge p-2 variant-soft-tertiary">3. offline</span>
								<span class="flex-auto">Verify & Sign the petition</span>
							</li>
							<li>
								<span class="badge p-2 variant-soft-primary">4. online</span>
								<span class="flex-auto">Scan the signature QR code</span>
							</li>
							<li>
								<span class="badge p-2 variant-soft-primary">5. online</span>
								<span class="flex-auto">Ask to commit the petition</span>
							</li>
						</ol>
					</div>
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
	
	
	<hr class="!border-t8" 
		style="
			border-style: dotted;
			border-top-width: 0.2cm;
			margin: 0.5cm 0;
		" 
	/>
	
	
	<div
		style="
			text-align: center;
			
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
			grid-template-rows: auto;
			gap: 10px;
		"
	>
		<span class="badge variant-soft"
			style="
				position: relative;
				
				font-size: 1.2em;
			"
		>
			<span>Net Name</span>
			<span 
				icann_net_name
				class="badge variant-filled-surface"
			>{ freight.fields.net_name }</span>
		</span>
		<span class="badge variant-soft"
			style="
				position: relative;
				
				font-size: 1.2em;
			"
		>
			<span>Net Path</span>
			<span 
				icann_net_path
				class="badge variant-filled-surface"
			>{ freight.fields.ICANN_net_path }</span>
		</span>
		<span class="badge variant-soft"
			style="
				position: relative;
				
				font-size: 1.2em;
			"
		>
			<span>Function</span>
			<span class="badge variant-filled-surface">0x1::aptos_account::transfer</span>
		</span>
	</div>

	<hr class="!border-t8" 
		style="
			border-style: dotted;
			border-top-width: 0.2cm;
			margin: 0.5cm 0;
		" 
	/>
	
	<div 
		from_aptos_address
		class="card variant-soft-primary p-2" 
		style="color: inherit"
	>
		
		
		<Address_Qualities_Trinket 
			name="From Address"
			bind:this={ origin_address_trinket }
			on_change={ on_change_origin_address }
			on_prepare={ on_prepare_origin_address }
		/>
	</div>
	
	<div style="height: 0.5cm"></div>
		
	<div 
		to_aptos_address
		class="card variant-soft-primary p-2" 
		style="color: inherit"
	>
		<Address_Qualities_Trinket 
			name="To Address"
			bind:this={ to_address_trinket }
			on_change={ on_change_to_address }
			on_prepare={ on_prepare_to_address }
		/>
	</div>

	<div style="height: 0.5cm"></div>

	<div class="card variant-soft-primary p-4" style="color: inherit">
		<div style="text-align: center;">
			<span 
				class="badge variant-soft-primary" 
				style="
					margin: 0 auto;
					padding: 0.2cm 1cm;
				"
			>
				<p style="font-size: 1.2em; font-weight: bold;">Amount</p>
			</span>
		</div>
		
		<p
			style="text-align: center; padding-bottom: 10px"
		>1 APT = 1e8 Octas</p>
		
		<Amount_Field 
			on_change={ on_amount_change }
		/>
	</div>

	<div style="height: 0.2cm"></div>
	
	<div 
		class="card variant-soft-primary p-1" 
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
		>Seconds until Expiration</span>
		
		<label class="label"
			style="display: flex; align-items: center;"
		>
			<input 
				class="input"
				style="
					text-indent: 10px; 
					padding: 0.1cm;
					padding-right: 0.3cm;
				" 
				
				transaction_expiration
				placeholder="" 
				
				type="number" 
				bind:value={ freight.fields.transaction_expiration }
			/>
		</label>
	</div>

	<div style="height: 0.2cm"></div>
	
	<div
		class="card variant-soft-primary p-1" 
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
		>Gas Unit Price, in Octas</span>
		
		<label class="label"
			style="display: flex; align-items: center;"
		>
			<input 
				transaction_expiration
			
				class="input"
				style="
					text-indent: 10px; 
					padding: 0.1cm;
					padding-right: 0.3cm;
				" 
				
				
				placeholder="" 
				
				type="number" 
				bind:value={ freight.fields.gas_unit_price }
			/>
		</label>
	</div>
	
	<div style="height: 0.2cm"></div>
	
	<Field 
		logo="Max Gas Amount, in Octas"
		
		bind:this={ max_gas_amount_field }
		on_change={ max_gas_amount_on_change }
		on_prepare={ max_gas_amount_on_prepare }
	/>
</div>
{/if}