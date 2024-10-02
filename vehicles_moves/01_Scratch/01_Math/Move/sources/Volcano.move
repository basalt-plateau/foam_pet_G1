




module founder::Math_1 {
	
	//
	//
	/* Views */
	//
	//	
	/*
		views: integer math
			https://aptos.dev/en/build/smart-contracts/book/integers#arithmetic
	*/
	#[view]
	public fun add_integers (integer_1: u256, integer_2: u256): u256 {
		let sum = integer_2 + integer_1;
		sum
	}
	#[view]
	public fun multiply_integers (integer_1: u256, integer_2: u256): u256 {
		let product = integer_2 * integer_1;
		product
	}
	#[view]
	public fun divide_integers (dividend: u256, divisor: u256): u256 {
		let quotient = dividend / divisor;
		quotient
	}
}
