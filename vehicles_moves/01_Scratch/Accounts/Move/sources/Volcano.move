




module pilot::Map_2 {
	
	
	use aptos_framework::block;
	
	
	struct Place {}
	struct Map {}
	
	
	

	/*
		views: map
	*/
	#[view]
	public fun ask_latest_block (): u64 {
		let current_block_height = block::get_current_block_height ();
		current_block_height
	}
}
