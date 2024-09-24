




module founder::Octas_1 {
	
	use aptos_framework::coin;
	
	
	
	
	/*
		Similar:
			0x1::coin::transfer
			
		CoinTypes: 
			0x1::aptos_coin::AptosCoin
	*/
	public entry fun give <CoinType> (
		sender: &signer, 
		recipient: address, 
		amount: u64
	) {
		let coins = coin::withdraw<CoinType>(sender, amount);
		coin::deposit (recipient, coins);
	}
	
	
	
	
	/*
		views: balance
	*/
	#[view]
    public fun ask_address_balance <Coin> (account_address: address): u64 {
        let balance: u64 = coin::balance<Coin>(account_address);
		balance
    }
}
