


<script>

//\\
//
import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';	
import { TreeView, TreeViewItem, RecursiveTreeView } from '@skeletonlabs/skeleton';
import { Accordion, AccordionItem } from '@skeletonlabs/skeleton';
//
//
import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'
import Slang from '$lib/trinkets/Slang/Trinket.svelte'
import Installation_with_Docker from '$lib/trinkets/Wild/Docker/Trinket.svelte'
import Code_Wall from '$lib/trinkets/Code_Wall/Trinket.svelte' 
//
//
import Beacons from './Beacons/Trinket.svelte'
//
////

import Relatives from '$lib/Letters/Relatives.svelte'


/*
let relatives_name = (
	"家庭"	
)
*/


/*
// 
//
//
//
//
var relatives_name = (
	"ᎤᏓᏅᏙᏗ"
)
var relatives_language = "Cherokee";
var relatives_pronunciation = "udanvdo"


// 
//
//
//
//
let relatives_name = (
	"ᐊᔭᖅ"
)
let relatives_language = "Inuktitut";
let relatives_pronunciation = "ajaaq"
*/


// 
//
//
//
//
var relatives_name = "Foam"
var relatives_language = "Foam Pet";
var relatives_pronunciation = ""




let tabSet = 0

</script>



<svelte:head>
	<title>{ relatives_name }</title>
	<meta name="description" content="About this app" />
</svelte:head>


<Leaf>
<div 
	style="
		display: flex;
		flex: 0.6;
		justify-content: center;
		flex-direction: column;
		min-height: 100%;
	"
>
	<div
		class="card p-1"
		style="
			width: 100%;
		"
	>
		<p
			style="
				text-align: center;
				display: flex;
				align-items: center;
				justify-content: center;
			"
		>
			<span
				style="
					display: inline-flex;
					align-items: center;
				"
			><Relatives /></span>
			<span style="width: 10px"> </span>
			<span>might be { relatives_language } for "relatives".</span>
		</p>
	</div>

	<div style="height: 0.2cm"></div>

	<div
		class="card p-4"
		style="
			padding: 1cm;
			width: 100%;
		"
	>
		<header
			style="
				display: none;
				font-size: 2.5em;
				text-align: center;
			"
		>{ relatives_name }</header>
				
		<p
			style="
				text-align: center;
				font-size: 1.2em;
			"
		>These activities should happen offline.</p>
		
		<div style="height: 0.25cm"></div>
		
		<p style="text-align: center">
			The QR code interface should be used.
		</p>
		
		<div style="height: 0.25cm"></div>
		
		<div
			class="card variant-soft-surface p-4"
			style="
				max-width: 15cm;
				margin: 0 auto;
			"
		>
			<ol class="list">
				<li>
					<span class="badge-icon p-4 variant-soft-primary">1</span>
					<span class="flex-auto">
						<Slang text="Accounts"/> is for choosing an <Slang text="Account"/>
					</span>
				</li>
				<li>
					<span class="badge-icon p-4 variant-soft-primary">2</span>
					<span class="flex-auto"><Slang text="Signatures"/> is for signing for Friends Vacations</span>
				</li>
			</ol>
		</div>
	</div>
	
	<!-- 
	<div style="height: 0.5cm"></div>
	<Beacons /> 
	
	
	<div style="height: 0.5cm"></div>
	<Installation_with_Docker />
	-->
	
	<div style="height: 1cm"></div>

</div>
</Leaf>