


<script>

/*
	import Slang_Cipher from '$lib/trinkets/Slang/Cipher.svelte'
	<Slang_Cipher />
*/

import { has_field } from 'procedures/object/has_field'
import { onMount } from 'svelte'
import nlp from 'compromise/one'
import { nocturnalize } from './screenplays/nocturnalize'

import { English_1 } from './jargons/English_1'


const organize_slang = (bracket) => {
	const sorted_by_keys = Object.keys (bracket).sort ();
	
	const organized = {};
	for (const key of sorted_by_keys) {
		organized [key] = bracket [key];
	}
	
	return organized
}

const organized = organize_slang (English_1)

console.log ({ organized })

</script>


<div>
	
	
	
	<div class="table-container">
		<table class="table table-hover">
			<thead>
				<tr>
					<th style="width: 6cm">Slang</th>
					<th>Jingle</th>
				</tr>
			</thead>
			<tbody>
				{#each Object.entries (organized) as [ saying, equivalent ]}
					<tr>
						<td>{ equivalent }</td>
						<td>{ saying }</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>