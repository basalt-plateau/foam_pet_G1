





////
//
import * as AptosSDK from "@aptos-labs/ts-sdk";
//
//
import { has_field } from 'procedures/object/has_field'
//
//
import { build_truck } from '$lib/trucks'
import { parse_styles } from '$lib/trinkets/styles/parse'
//
//
import { the_ledger_ask_loop_creator } from './Screenplays/is_connected'
//
////

import { rhythm_filter } from 'procedures/dates/rhythm-filter'


let the_ledger_ask_loop;

const trucks = {}

//
//
//	maybe this
//
//
const monitor_local_storage = () => {}


var window_size_changed;
const monitor_window = ({ truck }) => {
	console.log ({ truck })	
	
	var RF = rhythm_filter ({
		every: 200
	});
	window_size_changed = (event) => {
		RF.attempt (({ ellipse, is_last }) => {
			console.log ("window size changed", { event })
			
			truck.freight.window_width = window.innerWidth;
		});
	}

	window.addEventListener ("resize", window_size_changed);
}


export const lease_roomies_truck = () => {
	const the_domain = window.location.hostname;
	
	let net_path = "https://api.mainnet.aptoslabs.com/v1"
	let net_name = "mainnet"
	let mode = "business"
	
	
	
	
	// let origin_address = "http://localhost:22000"
	// let origin_address = "https://" + the_domain;
	// let origin_address = "/";
	let origin_address = "https://foam.hair";
	
	if (typeof localStorage.net_name === "string") {
		net_name = localStorage.net_name	
	}
	if (typeof localStorage.net_path === "string") {
		net_path = localStorage.net_path	
	}
	if (typeof localStorage.mode === "string") {
		mode = localStorage.mode	
	}
	if (typeof localStorage.origin_address === "string") {
		origin_address = localStorage.origin_address	
	}
	
	
	trucks [1] = build_truck ({
		freight: {
			/*
				business: 
					The actual mode of the package that's sent.
				
				nurture: 
					For building, this has features that are being raised.
				location
				[ "nurture", "business" ]
				 
				import { check_roomies_truck } from '$lib/Versies/Trucks'
				const mode = check_roomies_truck ().freight.mode;
				{#if mode === "nurture" }
				{/if}
			*/
			//mode: "business",
			mode,
			
			origin_address,
			
			net_path,
			net_name,
			net_connected: "no",
			
			window_width: window.innerWidth,
			
			layout: {
				leaf_styles: parse_styles ({
					margin: '0 auto',
					'max-width': '64rem',
					width: '100%'
				})
			},
			
			aptos: new AptosSDK.Aptos (
				new AptosSDK.AptosConfig ({		
					fullnode: net_path,
					network: AptosSDK.Network.CUSTOM
				})
			)
		}
	})
	
	
	monitor_window ({
		truck: trucks [1]
	});
	
	the_ledger_ask_loop = the_ledger_ask_loop_creator ();
	the_ledger_ask_loop.play ();
}



export const ask_for_freight = () => {
	return trucks [1].freight;
}
export const give_back_roomies_truck = () => {
	the_ledger_ask_loop.stop ();
	window.removeEventListener ("resize", window_size_changed)
	delete trucks [1];
}
export const check_roomies_truck = () => {
	return trucks [1];
}
export const monitor_roomies_truck = (action) => {	
	return trucks [1].monitor (({ freight }) => {
		// console.info ('Seeds Truck_Monitor', { freight })
		
		localStorage.setItem ("location", JSON.stringify (freight.location))
		
		action (freight);
	})
}







