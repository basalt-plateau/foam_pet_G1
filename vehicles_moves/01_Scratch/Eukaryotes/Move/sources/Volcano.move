






module Fest::Eukaryotes_1 {
	
	use aptos_framework::block;
	use std::string::{Self, String};

	/*
		views: dream
	*/
	#[view]
	public fun rules_1 () : vector<u8> {
		let rules = b"This is an organism floating through the multiverse.";
		rules
	}
	
	#[view]
	public fun rules_2 () : String {
		let rules = b"This is an organism floating through the multiverse.";
		string::utf8 (rules)
	}
}
