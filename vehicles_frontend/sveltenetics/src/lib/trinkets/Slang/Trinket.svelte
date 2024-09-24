

<script>

/*
	import Slang from '$lib/trinkets/Slang/Trinket.svelte'
	<Slang text="transaction" />
*/

/*
	Currently supports replacing 1 or 2 word sayings.
*/

/*
	@ Legend
		@ Vernacular
		@ Jargon
*/

/*
	Decipher Aristocratic English into Regular English.
*/

/*
	
*/

import { has_field } from 'procedures/object/has_field'
import { onMount } from 'svelte'
import nlp from 'compromise/one'
import { nocturnalize } from './screenplays/nocturnalize'

import { English_1 } from './jargons/English_1'

const language = "English"
const legend = {
	"Chinese": {},
	"Francais": {},
	"Spanish": {},
	
	"English": English_1,
}

// let legendary = legend [ language ] [ text ]
let legend_language = legend [ language ]


export let style = ""
export let text = ""
$: {
	let _text = text;
	built = nocturnalize ({ legend_language, text })
}

var built = []


onMount (() => {
	built = nocturnalize ({ legend_language, text })
})


let actual_styles = `
	color: inherit;
			
	font-weight: bold;
	font-size: 1em;
` + style;

</script>




<span>
	{#each built as part }
	{#if part.code === "yes"}
		<span><code
			class="code"
			style={ actual_styles }
		>{ part.text }</code></span>
	{:else}
		<span>{ part.text }</span>
	{/if}
	{/each}
</span>
