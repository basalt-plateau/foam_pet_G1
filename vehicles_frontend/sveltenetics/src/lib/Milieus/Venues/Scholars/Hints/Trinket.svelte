

<script>

////
//
import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';
//
//
import Panel from '$lib/trinkets/panel/trinket.svelte'
import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'
import Slang from '$lib/trinkets/Slang/Trinket.svelte'
import Caution from '$lib/trinkets/_Caution/Trinket.svelte'
//
import Offline_Machine_Tutorial from '$lib/places/Scholars/Offline_Machine_Tutorial.svelte'
import Online_Machine_Tutorial from '$lib/places/Scholars/Online_Machine_Tutorial.svelte'
import Orbital_Wallet_Tutorial from '$lib/places/Scholars/Orbital_Wallet_Tutorial.svelte'
//
import { check_roomies_truck } from '$lib/Versies/Trucks'
import Slang_Cipher from '$lib/trinkets/Slang/Cipher.svelte'
import Milieus_Button from '$lib/Milieus/Button/Trinket.svelte'
//
////


import Preparation_Tutorial from './Preparation_Tutorial/Trinket.svelte'
	
	
////
//
const tutorial_2 = '/pictures/tutorial_2.svg';
const machines_picture = '/pictures/machines.svg';
const pets = '/pictures/Foam_pet.svg';
const pet = '/pictures/pet.svg';
const pet_2 = '/pictures/pet_2.svg';

//
////

const mode = check_roomies_truck ().freight.mode;		

/*
let seeds_name = (
	"পণ্ডিত"
)
*/




let seeds_name = (
	"அறிஞர்கள்"
);
let seeds_language = "Tamil";
let seeds_pronunciation = "aṟiñarhal";


/*
let seeds_name = (
	"විද්‍යාපීඨ"
);
let seeds_language = (
	"Sinhala"
);
*/

</script>

<svelte:head>
	<title>{ seeds_name }</title>
</svelte:head>


<style>
.accordion-control {
}

</style>


<Leaf>
	<div
		class="card p-1"
		style="
			width: 100%;
		"
	>
		<p
			style="
				text-align: center;
			"
		>"{ seeds_name }", pronounced { seeds_pronunciation }, might be { seeds_language } for "scholars".</p>
	</div>

	<div style="height: 0.5cm"></div>

	<div class="card p-4">
		<div style="height: 1cm"></div>
	
		<header 
			style="
				display: flex;
				justify-content: center;
				align-items: center;
				gap: 5%;
				
				margin: 0 auto;
				
				width: 100%;
				max-width: 600px;
				
				
			
				font-size: 2.5em; 
				text-align: center;
				font-family: sans-serif !important;
			"
		>
			<img 
				style="
					height: 1cm;
				"
				src={ pet } 
				alt="pet" 
			/>
			
			<Slang text="Label" style="font-family: serif;" />
			
			<img 
				style="
					height: 1cm;
				"
				src={ pet_2 } 
				alt="pet 2" 
			/>
		</header>
		
		
		
		<div style="height: 1cm"></div>
	</div>

	<div style="height: 0.5cm"></div>

	<div
		class="card p-4"
		style="
			width: 100%;
		"
	>	
		<div
			style="
				display: flex;
				border-radius: 4px;
				justify-content: center;
			"
		>
			<img src={ pets } alt="Machines" />
		</div>
		<div 
			style="
				display: flex;
				justify-content: center;
				flex-direction: row;
			"
		>
			<div 
				style="width: 50%"
				class="card p-4"
			>
				<p
					style="text-align: center"
				><Slang text="Offline Machine" /></p>
				<p style="font-size: 1em; text-align: center; line-height: 2em">
					<span class="badge variant-soft-primary">% Offline Machine</span>
					<span class="badge variant-soft-primary">% Offline Computer</span>
					<span class="badge variant-soft-primary">% Beacon with Limited Connectivity</span>
					<span class="badge variant-soft-primary">% Key Ring</span>
				</p>
			</div>
			
			<div 
				style="width: 1%"
			></div>
			
			<div 
				style="width: 50%"
				class="card p-4"
			>
				<p
					style="text-align: center"
				><Slang text="Online Machine" /></p>
				<p style="font-size: 1em; text-align: center; line-height: 2em">
					<span class="badge variant-soft-primary">% Online Machine</span>
					<span class="badge variant-soft-primary">% Online Computer</span>
					<span class="badge variant-soft-primary">% Internet Connected Beacon</span>
					<span class="badge variant-soft-primary">% SOS Beacon</span>
					<span class="badge variant-soft-primary">% Howl Beacon</span>
				</p>
			</div>
		</div>
	</div>
	
	<div style="height: 0.5cm"></div>

	<div class="card p-4">
		<div style="height: 1cm"></div>
	
		<div style="font-size: 1em; text-align: center; line-height: 2em;">
			<p
				
			>
				<span><Slang text="Labels" /> can interact with <Slang text="Aptos" />.</span>
			</p> 
			<p>
				<a class="anchor" href="https://Aptos.dev">https://Aptos.dev</a>
			</p>
			<p>
				<a class="anchor" href="https://aptosfoundation.org">https://aptosfoundation.org</a>
			</p>
		</div>
	
		<div style="height: 1cm"></div>
	
		<p
			style="font-size: 1em; text-align: center; line-height: 2em;"
		>
			<span><Slang text="Labels" /> know how to drive an Offline Wallet (Cold Wallet, Airgapped Wallet)</span>
			<br />
			<span>from an <Slang text="Offline Machine" />.</span>
		</p> 
		
		<div style="height: 1cm"></div>
		
		<p
			style="font-size: 1em; text-align: center; line-height: 2em;"
		>
			<span><Slang text="Labels" /> are friendly</span>
			<br />
			<span>from <Slang text="Online_Machines" />.</span>
		</p> 
		
		<div style="height: 1cm"></div>
		
		<div style="text-align: center;">
			<span>A <Slang text="Label" /> can be adopted from </span>
			
			<Milieus_Button
				name={ "Wild" }
				location={[ "Scholars", "Wild" ]}
				is_open_location={[ "Scholars", "Wild" ]}
				style="display: inline-block"
			/>
		</div>
		
		<div style="height: 1cm"></div>
	</div>
	
	<div style="height: 1cm"></div>
	
	<div class="card p-4">
		<div style="height: 1cm"></div>
		<p
			style="font-size: 1em; text-align: center"
		>
			<span>An offline machine can communicate with an online machine with a QR code signatures.</span>			
		</p> 
		
		<div style="height: 1cm"></div>
		
		<p
			style="font-size: 1em; text-align: center"
		>
			Private Key + Petition -> Signature
		</p>

		<div style="height: 1cm"></div>
		
		<p
			style="font-size: 1em; text-align: center"
		>
			<span>Thus, the <Slang text="Private Key" /> nevers needs to be sent to an online machine.</span>
		</p>
		
		<div style="height: 1cm"></div>
		
		<div class="card p-2 variant-soft">
			<Accordion>
				<AccordionItem>
					<svelte:fragment slot="summary">
						<div
							style="
								text-align: center;
								font-size: 1.5em;
							"
						>
							<p>Offline Signing Tutorial</p>
						</div>
					</svelte:fragment>
					<svelte:fragment slot="content">
						<Orbital_Wallet_Tutorial />
					</svelte:fragment>
				</AccordionItem>
			</Accordion>
		</div>
		
		<div style="height: 1cm"></div>
	</div>
	
	
	<div style="height: 0.5cm"></div>
	
	
	<div class="card p-4">		
		<div style="height: 0.25cm"></div>
		
		<div class="card p-2 variant-soft">
			<Accordion>
				<AccordionItem>
					<svelte:fragment slot="summary">
						<div>
							<p><Slang text="Offline Machine" /> Tutorial</p>
						</div>
					</svelte:fragment>
					<svelte:fragment slot="content">
						<Offline_Machine_Tutorial />
					</svelte:fragment>
				</AccordionItem>
			</Accordion>
		</div>
		
		<div style="height: 0.25cm"></div>
		
		<div class="card p-2 variant-soft">
			<Accordion>
				<AccordionItem>
					<svelte:fragment slot="summary">
						<div>
							<p><Slang text="Online Machine" /> Tutorial</p>
						</div>
					</svelte:fragment>
					<svelte:fragment slot="content">
						<Online_Machine_Tutorial />
					</svelte:fragment>
				</AccordionItem>
			</Accordion>
		</div>
	</div>
	
	
	<div style="height: 0.5cm"></div>
	
	<div class="card p-4">
		<header 
			style="
				font-size: 2em; 
				text-align: center;
				padding: 0cm 0;
			"
		>Regions</header>
		
		<div style="height: 0.5cm" ></div>
		<hr class="!border-t-2" />
		<div style="height: 0.5cm" ></div>
		
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<header 
						style="
							font-size: 1.5em; 
							text-align: center;
							padding: 0cm 0;
						"
					>Scholars</header>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div>
						<p
							style="font-size: 1em; text-align: center"
						>	
							<span>The <b>Scholars</b> region has features that affect the local browser.</span>
						</p>
					</div>
				</svelte:fragment>
			</AccordionItem>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<header 
						style="
							font-size: 1.5em; 
							text-align: center;
							padding: 0cm 0;
						"
					>Relatives</header>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div>
						<p
							style="font-size: 1em; text-align: center"
						>	
							<span>The <b>Relatives</b> region should be used on a <Slang text="Offline Machine" /></span>
						</p>
					</div>
				</svelte:fragment>
			</AccordionItem>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<header 
						style="
							font-size: 1.5em; 
							text-align: center;
							padding: 0cm 0;
						"
					>Friends</header>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div>
						<p
							style="font-size: 1em; text-align: center"
						>	
							<span>The <b>Friends</b> region should be used on a <Slang text="Online Machine" /></span>
						</p>
					</div>
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
	
	<div style="height: 0.5cm"></div>

	<div class="card p-4">
		<header 
			style="
				font-size: 2em; 
				text-align: center;
				padding: 0.5cm 0;
			"
		>Slanguage</header>
		<p
			style="
				text-align: center;
			"
		>
			Slang that appear like these <Slang text="Consensus" />, <Slang text="Transaction" />, <Slang text="Online Machine" />
			<span>have equivalent jingles.</span>
			
			
		</p>
		
		<div style="height: 0.5cm"></div>
		
		<Accordion>
			<AccordionItem>
				<svelte:fragment slot="summary">
					<div
						style="
							text-align: center;
							font-size: 1.5em;
						"
					>
						<p>Mottos</p>
					</div>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<Slang_Cipher />
				</svelte:fragment>
			</AccordionItem>
		</Accordion>
	</div>
	
	<div style="height: 0.5cm"></div>
	
	<div
		class="card p-4"
		style="
			margin: 0 auto;
		"
	>
		<ol class="list">
			<li>
				<span class="badge p-4 variant-soft-primary">Anatomy</span>
				<span 
					style="
						line-height: 2em;
					"
					class="flex-auto"
				>
					<a 
						style="display: block"
						class="anchor" 
						href="https://gitlab.com/basalt_plateau/foam_pet"
						target="_blank"
					>https://gitlab.com/basalt_plateau/foam_pet</a>
					<a 
						style="display: block"
						class="anchor" 
						href="https://github.com/basalt-plateau/foam_pet"
						target="_blank"
					>https://github.com/basalt-plateau/foam_pet</a>
				</span>
			</li>
		</ol>
	</div>
	
	<div style="height: 5cm"></div>
</Leaf>

