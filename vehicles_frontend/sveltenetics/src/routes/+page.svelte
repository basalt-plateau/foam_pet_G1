

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
//
import Offline_Machine_Tutorial from '$lib/places/Scholars/Offline_Machine_Tutorial.svelte'
import Online_Machine_Tutorial from '$lib/places/Scholars/Online_Machine_Tutorial.svelte'
import Orbital_Wallet_Tutorial from '$lib/places/Scholars/Orbital_Wallet_Tutorial.svelte'
//
//
import { check_roomies_truck } from '$lib/Versies/Trucks'
//
////

////
//
const tutorial_2 = '/pictures/tutorial_2.svg';
const machines_picture = '/pictures/machines.svg';
//
////

const mode = check_roomies_truck ().freight.mode;		



</script>

<svelte:head>
	<title>Hints</title>
</svelte:head>



<Leaf>
	<Panel styles={{
		'margin': '4px',
		'width': '100%',
		'padding': '0.5cm'
	}}>
		<header 
			style="
				font-size: 2em; 
				text-align: center;
				padding: 0.5cm 0.25cm;
			"
		><Slang text="Label" /></header>
		
		<p
			style="
				display: none;
				font-size: 1em; 
				text-align: center;
			"
		><i>Unless you run a Node, you shouldn't have to know anything about cybersecurity.</i></p>
		
		<p
			style="font-size: 1em; text-align: center"
		>This <Slang text="Label" /> is a <Slang text="Friends_Habitat" /> + a <Slang text="Relatives_Habitat" />.</p>

		
		<div style="height: 0.25cm"></div>
		<hr class="!border-t-2" />
		<div style="height: 0.25cm"></div>
		
		<p style="font-size: 1em; text-align: center">
			<span>To keep <Slang text="Private Keys" /> obscure,<br/></span>
			<span>this <Slang text="Label" /> requires 2 <Slang text="Machines" /></span>
		</p>
		
		<div style="height: 0.25cm"></div>
		<hr class="!border-t-2" />
		<div style="height: 0.25cm"></div>
		
		<div
			style="
				display: flex;
				border-radius: 4px;
				justify-content: center;
			"
		>
			<img src={ machines_picture } alt="Machines" />
		</div>
		<div 
			style="
				display: flex;
				justify-content: center;
				flex-direction: row;
			"
		>
			<div
				style="
					width: 49%;
					display: flex;
					justify-content: center;
					flex-direction: column;
				"
				
			>
				<div class="card p-4">
					<p
						style="text-align: center"
					><Slang text="Offline Machine" /></p>
					<p style="font-size: 1em; text-align: center">
						<span class="badge variant-filled-primary">@ Offline Machine</span>
						<span class="badge variant-filled-primary">@ Offline Computer</span>
						<span class="badge variant-filled-primary">@ Device with Limited Connectivity</span>
					</p>
					
				</div>
				
				<div style="height: 0.25cm"></div>
				
				<div class="card p-4">
					<p
						style="text-align: center"
					><Slang text="Relatives_Habitat" /></p>
					<p style="font-size: 1em; text-align: center">
						<span class="badge variant-filled-primary">@ Cold Wallet</span>
						<span class="badge variant-filled-primary">@ Offline Wallet</span>
						<span class="badge variant-filled-primary">@ Airgapped Wallet</span>
					</p>
				</div>
				
			</div>
			
			
			
			<span 
				style="
					height: 100px;
				"
				class="divider-vertical" 
			/>
			
			<div
				style="
					width: 49%;
					display: flex;
					flex-direction: column;
				"
			>
				<div class="card p-4">
					<p
						style="text-align: center"
					><Slang text="Online Machine" /></p>
					<p style="font-size: 1em; text-align: center">
						<span class="badge variant-filled-primary">@ Online Machine</span>
						<span class="badge variant-filled-primary">@ Online Computer</span>						
						<span class="badge variant-filled-primary">@ Internet Connected Device</span>
					</p>
				</div>
				
				<div style="height: 0.25cm"></div>
				
				<div class="card p-4">
					<p
						style="text-align: center"
					><Slang text="Friends_Habitat" /></p>
					<p style="font-size: 1em; text-align: center">
						<span class="badge variant-filled-primary">@ Forum</span>
					</p>
				</div>
			</div>
		</div>
		
		
		<div style="height: 0.25cm"></div>
		
		
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
							<p><Slang text="Accounts" /> Tutorial</p>
						</div>
					</svelte:fragment>
					<svelte:fragment slot="content">
						
					</svelte:fragment>
				</AccordionItem>
			</Accordion>
		</div>
		
		<div style="height: 0.25cm"></div>
		
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
							<p>Giving APT Tutorial</p>
						</div>
					</svelte:fragment>
					<svelte:fragment slot="content">
						<Orbital_Wallet_Tutorial />
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
	</Panel>
	
	<div style="height: 0.5cm"></div>
	
	<Panel styles={{
		'display': 'none',
		
		'margin': '4px',
		'width': '100%',
		'padding': '0.5cm'
	}}>
		<div
			style="
				border-radius: 4px;
				
				
				display: flex;
				justify-content: center;
			"
		>
			<img src={ tutorial_2 } alt="My Icon" />
		</div>
	</Panel>
	
	<div style="height: 0.5cm"></div>
	
	<Panel styles={{
		'margin': '4px',
		'width': '100%',
		'padding': '0.5cm'
	}}>
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
					>Seeds</header>
				</svelte:fragment>
				<svelte:fragment slot="content">
					<div>
						<p
							style="font-size: 1em; text-align: center"
						>	
							<span>The <b>Seeds</b> region has features that affect the local browser.</span>
						</p>
						<p
							style="font-size: 1em; text-align: center"
						>
							<span>The features can be changed at </span>
							<a 
								class="anchor" 
								href="/Seeds/Features"
								target="_blank"
							>/Seeds/Features</a>
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
	</Panel>
	
	<div style="height: 0.5cm"></div>
	
	<Panel styles={{
		'margin': '4px',
		'width': '100%',
		'padding': '0.5cm'
	}}>
		<header 
			style="
				font-size: 2em; 
				text-align: center;
				padding: 0.5cm 0;
			"
		>Equalities</header>
		<p
			style="
				text-align: center;
			"
		>
			Sayings that appear like these <Slang text="Consensus" />, <Slang text="Transaction" />, <Slang text="Online Machine" />
			<span>are slang that have equivalents.</span>
		</p>
	</Panel>
	
	<div style="height: 5cm"></div>
</Leaf>

<style>

</style>
