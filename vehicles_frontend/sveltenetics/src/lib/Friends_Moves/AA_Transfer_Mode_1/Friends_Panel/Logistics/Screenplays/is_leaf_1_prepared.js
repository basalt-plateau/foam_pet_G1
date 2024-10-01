

/*


*/


export const is_leaf_1_prepared = ({ freight }) => {
	return "yes"
	
	
	const { from_address_permitted } = freight.fields;
	if (from_address_permitted !== "yes") {
		// freight.current.note = `The "from" address isn't `
		
		console.log ("here!");
		
		return "no"
	}
	
	return "yes"
}