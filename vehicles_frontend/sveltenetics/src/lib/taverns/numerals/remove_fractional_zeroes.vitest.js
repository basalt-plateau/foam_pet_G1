

// vitest "lib/taverns/numerals/remove_fractional_zeroes.vitest.js"


import { remove_fractional_zeroes } from '$lib/taverns/numerals/remove_fractional_zeroes.js'

import { describe, it, expect } from 'vitest';
import assert from 'assert'

describe ("remove_fractional_zeroes", () => {
	it ("1", async () => {
		assert.equal (remove_fractional_zeroes ("1000"), "1")
		assert.equal (remove_fractional_zeroes ("100000000"), "1")
	});
})