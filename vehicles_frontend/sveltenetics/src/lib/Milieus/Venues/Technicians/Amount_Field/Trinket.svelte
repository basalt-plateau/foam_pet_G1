


<script>

/*	
	import Amount_Field from '$lib/trinkets/Amount_Field/Trinket.svelte'
	
	const on_amount_change = () => {}
	
	<Amount_Field 
		on_change={ on_amount_change }
	/>
*/

import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'


import Amount_Field from '$lib/trinkets/Amount_Field/Trinket.svelte'
const on_amount_change = ({ 
	effects,
	actual_amount_of_Octas
}) => {
	if (effects.problems === "") {
		
	}
}

</script>

<Leaf>
	<div class="card p-4">
		<Amount_Field 
			on_change={ on_amount_change }
		/>
	</div>
</Leaf>