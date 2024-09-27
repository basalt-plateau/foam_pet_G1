

<script>

import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';

import Slang from '$lib/trinkets/Slang/Trinket.svelte'
import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'


/*
	1. (Tough) Foam Pet Adoption.
	2. Choose a Ride
	3. Go on a vacation
*/

</script>


<div class="card p-4">
	<header
		style="
			font-size: 1.5em;
			text-align: center;
		"
	>Getting Moving</header>

	<div style="height: 0.5cm" />

	<div class="card p-2 variant-filled-primary">
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<div
						style="
							text-align: center;
							font-size: 1.5em;
						"
					>
						<p>1. (Tough) Foam Pet Adoption</p>
					</div>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div style="height: 0.5cm"></div>
				
					<div style="text-align: center;">
						<span>A <Slang text="Label" /> can be adopted from </span>
						
						<Milieus_Button
							name={ "Wild" }
							location={[ "Scholars", "Wild" ]}
							is_open_location={[ "Scholars", "Wild" ]}
							style="display: inline-block"
						/>
					</div>
					
					<div style="height: 0.5cm"></div>
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
	
	<div style="height: 0.5cm" />
	
	<div class="card p-2 variant-filled-primary">
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<div
						style="
							text-align: center;
							font-size: 1.5em;
						"
					>
						<p>2. Choose <Slang text="an_Account" /></p>
					</div>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<p style="text-align: center;">
						<span><Slang text="Accounts" /> are necessary for interacting with <Slang text="Aptos" />.</span>
					</p>
					
					<p style="text-align: center;">
						<span><Slang text="An_Account" /> can be found at</span>
						<Milieus_Button
							name={ "Rides" }
							location={[ "Relatives", "Rides" ]}
							is_open_location={[ "Relatives", "Rides" ]}
							style="display: inline-block"
						/>
					</p>
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
	
	<div style="height: 0.5cm" />
	
	<div class="card p-2 variant-filled-primary">
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<div
						style="
							text-align: center;
							font-size: 1.5em;
						"
					>
						<p>3. Go on a Vacation</p>
					</div>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<p style="text-align: center;">
						<span>Vacations can be found at</span>
						<Milieus_Button
							name={ "Vacations" }
							location={[ "Friends", "Vacations" ]}
							is_open_location={[ "Friends", "Vacations" ]}
							style="display: inline-block"
						/>
					</p>
					
					<p style="text-align: center;">
						<span>To allow a vacation, the vacation <Slang text="Petition" /> needs to be <Slang text="signed" /> for at</span>
						<Milieus_Button
							name={ "Signatures" }
							location={[ "Relatives", "Signatures" ]}
							is_open_location={[ "Relatives", "Signatures" ]}
							style="display: inline-block"
						/>
					</p>
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
</div>