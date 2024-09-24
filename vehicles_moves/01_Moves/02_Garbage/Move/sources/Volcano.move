


/*
	This is a lifeform orbiting a moon.
*/

module founder::Garbage_1 {
	
	// use 0x1::aptos_account;
	
	use std::signer;
	use std::vector;
	
	
	
	
	/*
		@ Unsigned Integer = @ Whole Numbers
		
	*/
	const W256_upper_limit: u256 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF;
	
	
	
	/*
		The error codes
	
	*/
	const Landfill_is_full: u64 = 1;
	const Landfill_has_zero_garbage: u64 = 2;
	
	
	//
	//
	/* Structures */
	//	https://aptos.dev/en/build/smart-contracts/book/abilities
	//
	struct Garbage has copy, drop, store, key {}
	
	
	/*
		2^256
	*/
	struct Landfill has copy, drop, store, key {
		size: u256,
		garbage: vector<Garbage>
	}
	
	/*
		Garbage in Features can be purchased.
	*/
	struct Feature has copy, drop, store, key {
		price: u256,
		garbage: Garbage
	}
	struct Features has copy, drop, store, key {
		size: u256,
		features: vector<Feature>
	}
	

	/* 
		Entry Runs 
			https://aptos.dev/en/build/smart-contracts/book/abilities
	*/
	/*
	
		With this, perhaps each address can have a landfill.	
	
	*/
	public entry fun build_global_landfill (vulture: &signer) {
		let size = 0;
		
        move_to<Landfill>(
			vulture, 
			Landfill {
				size: size,
				garbage: vector::empty<Garbage>()
			}
		);
    }
	
	
	
	/*
	
		This adds garbage to the landfilll.
	
	*/
	public entry fun add_garbage_to_landfill (vulture: &signer) acquires Landfill {
		let vulture_address = signer::address_of (vulture);
		let landfill = borrow_global_mut<Landfill>(vulture_address);
		let fresh_garbage = Garbage {};
		
		/*
			Asserts that the landfill
			isn't full.		
		*/
		assert! (landfill.size != W256_upper_limit, Landfill_is_full);
		
        vector::push_back (&mut landfill.garbage, fresh_garbage);
		landfill.size = landfill.size + 1;
    }
	
	
	/*
		
		Fabrication Zone:
			This adds garbage to the landfilll.
		
	*/
	public entry fun remove_garbage_from_landfill (vulture: &signer) acquires Landfill {
		let vulture_address = signer::address_of (vulture);
		let landfill = borrow_global_mut<Landfill>(vulture_address);
		
		/*
			Asserts that the landfill
			isn't full.		
		*/
		assert! (landfill.size != 0, Landfill_has_zero_garbage);
			
		
        vector::pop_back (&mut landfill.garbage);
		landfill.size = landfill.size - 1;
    }
	
	
	/* 
		Module Runs
	*/
    public fun ask_vulture_landfill_size (vulture: &signer): u256 acquires Landfill {
		let vulture_address = signer::address_of (vulture);
		borrow_global<Landfill>(vulture_address).size
    }
	
	
	/* 
		Views
	*/
	#[view]
	public fun ask_address_landfill_size (address_1: address): u256 acquires Landfill {
		borrow_global<Landfill>(address_1).size
    }
	
	
	
	
	/*
	public entry fun delete_module (
		account: &signer,
		module_address: address, 
		module_name: vector<u8>
	) {
		let signer_address = signer::address_of (account);
		let module_id = vector::empty<u8>();
		
		
	}
	*/
	
	
	
	
	
	
	//
	//
	/* Views */
	//
	//	
	
	
	
	
	
	
	
	
	
	
}
