


<script>

/*	

*/

import { onMount } from 'svelte'

import Leaf from '$lib/trinkets/Layout/Leaf/Trinket.svelte'
import Field from '$lib/trinkets/Field/Trinket.svelte'


let field = ""
const field_on_change = () => {
	
}



onMount (() => {
	
})


</script>

<Leaf>
	<div class="card p-4">
		<Field 
			logo="Max Gas Amount, in Octas"
	
			bind:this={ field }
			on_change={ field_on_change }
		/>
	</div>
</Leaf>