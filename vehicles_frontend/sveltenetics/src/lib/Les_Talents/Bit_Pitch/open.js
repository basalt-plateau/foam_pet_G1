

/*
	import { open_bit_throw } from '$lib/Les_Talents/Bit_Pitch/open'
	open_bit_throw ({ modal_store });
*/

import Bit_Pitch from './Trinket.svelte'

export const open_bit_throw = ({ modal_store }) => {
	modal_store.trigger ({
		type: 'component',
		backdropClasses: '!p-0 !fixed',
		component: {
			ref: Bit_Pitch,
			props: { 
				modal_store
			}
		}
	});
}