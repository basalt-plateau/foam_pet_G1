




module founder::Vectors_1 {
	

	/*
		Vectors:
			https://aptos.dev/en/build/smart-contracts/book/vector
	*/
	#[view]
	public fun vector_example (): vector<u64> {
		let vector_1 = vector::empty<u64>();
		
		// vector::destroy_empty(v);
		
		vector_1
	}
}
