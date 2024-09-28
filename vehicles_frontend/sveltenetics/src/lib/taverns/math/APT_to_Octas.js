

/*
	import { ask_convert_APT_to_Octas } from '$lib/taverns/math/APT_to_Octas.js'
	const { Octas } = await ask_convert_APT_to_Octas ({ APT })
*/

//
// APT: 1 			=== 1,0000,0000 Octas
// APT: 0.1			===   1000,0000 Octas
// APT: 0.01		===    100,0000 Octas
// APT: 0.001		===     10,0000 Octas
// APT: 0.0001		===      1,0000 Octas
// APT: 0.00001		===        1000 Octas
//

////
//
//	Highest:
//
//
//	Lowest:
//		APT: 0.00000001	-> 1 Octa
//
////

import { is_decimal_digit_string } from '$lib/taverns/numerals/decimal/is_string'
import { assert_is_natural_numeral_string } from '$lib/taverns/numerals/natural/is_string'

const valid_characters_1 = "01234567890."
const valid_characters_2 = "01234567890"


const assert_valid = ({ 
	APT,
	valid_characters = valid_characters_1 
}) => {
	if (typeof APT !== "string") {
		throw new Error (`APT amount needs to be a string, received: ${ typeof APT }`)
	}
	
	if (APT.length === 0) {
		throw new Error (`APT amount needs to be a string of length >= 1`)
	}
	
	//
	//
	//	Assert has exclusively characters: 01234567890.
	//
	//
	const last = APT.length - 1;
	for (let E = 0; E <= last; E++) {
		if (valid_characters.includes (APT [E]) !== true) {
			throw new Error (`APT amount needs to be a string, received: ${ typeof APT }`)
		}
	}
}


//
//
//  1234567 -> 1234570
//	1234 -> 12340000
//
//
export const add_zeroes = ({ fractional }) => {
	const zeroes = 8 - fractional.length;
	
	console.log ('adding zeroes:', { fractional, zeroes });
	
	for (let E = 1; E <= zeroes; E++) {
		fractional = fractional + "0";
	}
	
	return fractional;
}


//
//	 01234567 -> 1234567
//  001234567 -> 1234567
//
//
//	returns "0" if every digit is a zero
//
export const remove_leading_zeroes = ({ APT }) => {
	assert_is_natural_numeral_string (APT)
	
	
	
	
	let integer_as_string_end = APT.length - 1;
	// let integer_as_string_start = 0;
	
	let found_non_zero_1 = "no";
	
	let proceeds = ""
	for (
		let E = 0; 
		E <= integer_as_string_end;
		E++
	) {
		if (APT [E] !== "0") {
			found_non_zero_1 = "yes"
		}
		
		if (found_non_zero_1 === "yes") {
			proceeds += APT [E]
		}
		
		// console.log ({ proceeds })
	}
	
	if (proceeds.length === 0) {
		return "0"
	}
	
	return proceeds;
}


//
//	1234567000 -> 1234567
//  123456000  -> 123456
//
export const remove_fractional_zeroes = (Digit) => {
	assert_is_natural_numeral_string (APT)
	
	let integer_as_string_end = Digit.length - 1;
	// let integer_as_string_start = 0;
	
	let found_non_zero_1 = "no";
	
	let proceeds = ""
	for (
		let E = integer_as_string_end; 
		E >= 0;
		E--
	) {
		console.log ("Digit:", Digit [E])
		
		if (Digit [E] !== "0") {
			found_non_zero_1 = "yes"
		}
		
		if (found_non_zero_1 === "yes") {
			proceeds = Digit [E] + proceeds;
		}
	}
	
	return proceeds;
}

export const ask_convert_APT_to_Octas = ({ APT }) => {
	is_decimal_digit_string (APT)
	
	if (APT.includes (".") !== true) {
		return remove_leading_zeroes ({
			APT: APT + "00000000"
		})
	}
	
	const pair = APT.split (".")
	if (pair.length !== 2) {
		throw new Error (`The APT amount wasn't two parts after gettings the parts around the decimal.`)
	}
	
	const pair_fractional = add_zeroes ({ fractional: pair [1] })
	if (pair_fractional.length !== 8) {
		throw new Error (`The APT amount after the decimal was not 8 digits.`)
	}
	
	console.log ({ pair, pair_fractional })
	
	const squeeze = pair [0] + pair_fractional;
	
	return remove_leading_zeroes ({ APT: squeeze })

}


//