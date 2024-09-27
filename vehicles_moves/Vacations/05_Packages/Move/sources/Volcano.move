




/*
	This is a lifeform orbiting a moon.
*/

module founder::Packages_1 {
	
	use 0x1::package;
	use std::vector;
	
	public entry fun list_packages(): vector<address> {
		let packages = package::get_packages ();
		packages
	}
	
}
