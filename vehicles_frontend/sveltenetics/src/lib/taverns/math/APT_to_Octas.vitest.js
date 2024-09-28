



// vitest "lib/taverns/math/APT_to_Octas.vitest.js"



import { describe, it, expect } from 'vitest';

import assert from 'assert'

import { ask_convert_APT_to_Octas } from '$lib/taverns/math/APT_to_Octas.js'
import { remove_fractional_zeroes } from '$lib/taverns/math/APT_to_Octas.js'



describe ("APT to Octas drives", () => {
	describe ("remove_fractional_zeroes", () => {
		it ("1", async () => {
			assert.equal (remove_fractional_zeroes ("1000"), "1")
			assert.equal (remove_fractional_zeroes ("100000000"), "1")
		});
	})


	describe ("APT to Octas", () => {
		it.only ("without decimal", async () => {
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "000001233456789" }), "1233456789" + "00000000")
			
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "1" }), "100000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "2" }), "200000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "20" }), "2000000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "2000" }), "200000000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "298298" }), "298298" + "00000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "988988988988" }), "988988988988" + "00000000")
			assert.equal (await ask_convert_APT_to_Octas ({ 
				APT: "988988988988988988988988988988988988988988988" }), 
				"988988988988988988988988988988988988988988988" + "00000000"
			)
		});
		
		it ("with decimals", async () => {
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.1" }), "10000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.01" }), "1000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.001" }), "100000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.0001" }), "10000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.00001" }), "1000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.000001" }), "100")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.0000001" }), "10")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.00000001" }), "1")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.00000000" }), "0")
			
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "1.00000000" }), "1" + "00000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "1.10000000" }), "1" + "10000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "123.10000000" }), "123" + "10000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "1233456789.10000000" }), "1233456789" + "10000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "01233456789.10000000" }), "1233456789" + "10000000")
			assert.equal (await ask_convert_APT_to_Octas ({ APT: "000001233456789.10000000" }), "1233456789" + "10000000")
			
			
			
			// assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.01" }), "1000000")
		});
		
		
		it ("throws", async () => {
			
			
			assert_throw ("0.00000000001", `The APT amount after the decimal was not 8 digits.`)
			assert_throw ("0.0000000001", `The APT amount after the decimal was not 8 digits.`)
			assert_throw ("0.000000012", `The APT amount after the decimal was not 8 digits.`)
			
			
			assert_throw ("0.0.00000012", `The APT amount wasn't two parts after gettings the parts around the decimal.`)
			assert_throw ("000000012", `The APT amount wasn't two parts after gettings the parts around the decimal.`)

			
			// assert.equal (await ask_convert_APT_to_Octas ({ APT: "0.01" }), "1000000")
			
		});
	});
});