




<script>

/*
	@ Features
		@ Theme
	
		@ Attributes
		@ Characteristics
	
		@ Themes
		@ Rules
		@ Modes

	@ Plays
		@ Rules
		@ Theme
			@ Palette
*/

//\
//
import { onMount, onDestroy } from 'svelte'
import { AppRail, AppRailTile, AppRailAnchor } from '@skeletonlabs/skeleton';
import { LightSwitch } from '@skeletonlabs/skeleton';
import { RadioGroup, RadioItem } from '@skeletonlabs/skeleton';
import * as AptosSDK from "@aptos-labs/ts-sdk";
//
//
import Net_Choices_with_Text from '$lib/PTO/Nets/Choices_with_Text/Trinket.svelte'
import Panel from '$lib/trinkets/panel/trinket.svelte'
import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'
import { check_roomies_truck, monitor_roomies_truck } from '$lib/Versies/Trucks'
import Refresh_Browser_Storage from '$lib/Versies/Rules/Refresh_Browser_Storage.svelte'
//
///


import Scholars_Trucks from '$lib/Versies/Trucks.svelte'
import { trends } from './Trinket.js'


let seeds_freight = {}
let seeds_trucks_prepared = "no"
const on_seeds_truck_change = ({ freight: _freight, happening }) => {
	seeds_freight = _freight;
	if (happening === "mounted") {
		seeds_trucks_prepared = "yes"
	}
}


let net_prepare = () => {
	return {
		net_name: "mainnet"
	}
};
let every_net_enhance = ({
	net_name,
	net_path,
	net_connected,
	chain_id
}) => {
	console.info ('every_net_enhance', {
		net_name,
		net_path,
		chain_id
	})
	
	seeds_freight.net_path = net_path
	seeds_freight.net_name = net_name
	seeds_freight.aptos = new AptosSDK.Aptos (new AptosSDK.AptosConfig ({		
		fullnode: net_path,
		network: AptosSDK.Network.CUSTOM
	}));
};



/*
	
	Theme is part of 
	
*/
let theme = ""
let mounted = "no"
$: {
	let _theme = theme;
	change_theme ({ theme })
}
const change_theme = ({ theme: _theme }) => {
	console.log ("change_theme:", _theme)
	
	if (typeof _theme === 'string' && _theme.length >= 1) {
		localStorage.setItem ('body-theme', _theme);
		document.body.setAttribute ('data-theme', _theme)
		theme = _theme;
		
		console.log ({ _theme })
	}
}

const ask_for_theme = () => {
	let local_storage_theme = localStorage.getItem ('body-theme');
	if (
		typeof local_storage_theme === "string" &&
		local_storage_theme.length >= 1
	) {
		return local_storage_theme;
	}
	
	let body_theme = document.body.getAttribute ('data-theme') 
	if (
		typeof body_theme === "string" &&
		body_theme.length >= 1
	) {
		return body_theme;
	}
	
	return ''
}

onMount (() => {
	let theme = ask_for_theme ()
	
	change_theme ({ 
		theme
	});
	mounted = "yes"
});




</script>

<style>

@media (max-width: 600px) {
    .latest-block-panel {
		flex-direction: column !important;
	}
}
a {
	line-height: 110%;
}

</style>

<svelte:head>
	<title>Features</title>
	<meta name="description" content="Features" />
</svelte:head>

<Leaf>
	<Scholars_Trucks on_change={ on_seeds_truck_change } />
	{#if seeds_trucks_prepared === "yes" && mounted === "yes" }
	<div>		
		<div
			class="card p-4"
			style="
				display: flex;
				align-items: center;
				justify-content: center;
			"
		>
			<Net_Choices_with_Text 
				prepare={ net_prepare }
				every_enhance={ every_net_enhance }
			/>
		</div>
		
		<div style="height: 0.2cm"></div>
		
		<div
			class="card p-4"
			style="
				display: flex;
				align-items: center;
				justify-content: center;
				flex-direction: column;
			"
		>
			<div
				class="card p-2 variant-soft-surface"
				style="
					padding: 0.2cm 1cm;
					margin: 0.2cm 0 0.5cm;
				"
			>
				<header
					style="
						font-size: 1.4em;
						line-height: 100%;
					"
				>Beauty</header>
			</div>
			
			<div style="width: 10px"></div>
			<div
				class="card p-2 variant-filled-primary"
				style="
					display: flex;
					align-items: center;
					justify-content: center;
					gap: 8px;
				"
			>
				<div>Nocturnal</div>
				<LightSwitch />
				<div>Diurnal</div>
			</div>
			
			<div style="height: 0.2cm"></div>
			
			<RadioGroup>
				<RadioItem bind:group={theme} name="justify" value="Atolls">Atolls</RadioItem>
				<RadioItem bind:group={theme} name="justify" value="PTO">PTO</RadioItem>
				<RadioItem bind:group={theme} name="justify" value="rhubarb">Rhubarb</RadioItem>
				<RadioItem bind:group={theme} name="justify" value="Hacienda">Hacienda</RadioItem>
			</RadioGroup>
		</div>
		
		<div style="height: 0.2cm"></div>
		
		<Refresh_Browser_Storage />
		
		<div style="height: 4cm"></div>
	</div>
	{/if}
</Leaf>
