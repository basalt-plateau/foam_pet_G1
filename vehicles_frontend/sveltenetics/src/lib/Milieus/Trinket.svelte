

<script>


/*
	This shows the venue.
*/

/*	
	Important:
		Navigator
		Scholars_Truck
*/


import { onMount, onDestroy } from 'svelte'

import Milieus_Truck from '$lib/Milieus/Truck/Trinket.svelte'


////
//
//	Venues
//
//
import Scholars_Hints from './Venues/Scholars/Hints/Trinket.svelte'
import Scholars_Theme from './Venues/Scholars/Theme/Trinket.svelte'
import Scholars_Wild from './Venues/Scholars/Wild/Trinket.svelte'

import Friends_Talents from './Venues/Friends/Talents/Trinket.svelte'

import Loyals_Jerseys from './Venues/Loyals/Jerseys/Trinket.svelte'
import Loyals_Hints from './Venues/Loyals/Hints/Trinket.svelte'
import Loyals_Signatures from './Venues/Loyals/Signatures/Trinket.svelte'

import Technicians_Map from './Venues/Technicians/Trinket.svelte'
import Technicians_Address_Qualities from './Venues/Technicians/Address_Qualities/Trinket.svelte'
import Technicians_Address_Qualities_with_Address from './Venues/Technicians/Address_Qualities_with_Address/Trinket.svelte'
import Technicians_Amount_Field from './Venues/Technicians/Amount_Field/Trinket.svelte'
import Technicians_Consensus_Transactions from './Venues/Technicians/Consensus_Transactions/Trinket.svelte'
import Technicians_Hone_Focus from './Venues/Technicians/Hone_Focus/Trinket.svelte'
import Technicians_Net_Choices_with_Text from './Venues/Technicians/Net_Choices_with_Text/Trinket.svelte'
import Technicians_Net_Choices from './Venues/Technicians/Nets_Choices/Trinket.svelte'
import Technicians_Polytope from './Venues/Technicians/Polytope/Trinket.svelte'
import Technicians_Slang from './Venues/Technicians/Slang/Trinket.svelte'
import Technicians_Field from './Venues/Technicians/Field/Trinket.svelte'
//
////

let Milieus = {
	"Scholars": {
		"Hints": Scholars_Hints,
		"Wild": Scholars_Wild,
		"Theme": Scholars_Theme
	},
	"Friends": {
		"Talents": Friends_Talents
	},
	"Loyals": {
		"Hints": Loyals_Hints,
		"Jerseys": Loyals_Jerseys,
		"Signatures": Loyals_Signatures
	},
	"Technicians": {
		"Map": Technicians_Map,
		
		"Address Qualities": Technicians_Address_Qualities,
		"Address Qualities with Address": Technicians_Address_Qualities_with_Address,
		"Amount Field": Technicians_Amount_Field,		
		"Consensus Transactions": Technicians_Consensus_Transactions,		
		"Hone Focus": Technicians_Hone_Focus,		
		"Net Choices with Text": Technicians_Net_Choices_with_Text,		
		"Net Choices": Technicians_Net_Choices,		
		"Polytope": Technicians_Polytope,		
		"Slang": Technicians_Slang,
		
		"Field": Technicians_Field
	}
}

let location = []
let component = Milieus [ "Scholars" ] [ "Hints" ]

let Milieus_freight = {}
let Milieus_truck_prepared = "no"
const on_Milieus_truck_change = ({ freight: _freight, happening }) => {
	Milieus_freight = _freight;
	if (happening === "mounted") {
		Milieus_truck_prepared = "yes"
	}
	
	const location = Milieus_freight.location;
	
	console.log ("Milieus Location:", location [0], location [1])
	
	try {
		component = Milieus [ location [0] ] [ location [1] ]
	}
	catch (exception) {
		console.error (exception)
		
		component = Milieus [ "Scholars" ] [ "Hints" ]
	}
}




</script>



<div>	
	<Milieus_Truck on_change={ on_Milieus_truck_change } />
	
	{#if Milieus_truck_prepared === "yes" }
	<svelte:component this={ component } />
	{/if}
</div>
