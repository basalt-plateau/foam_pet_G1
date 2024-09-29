

<script>

/*
	import Field from '$lib/trinkets/Field/Trinket.svelte'

	let field = ""
	const field_on_change = () => {
		
	}
	
	<Field 
		logo="Max Gas Amount, in Octas"
		
		bind:this={ field }
		on_change={ field_on_change }
	/>
	
	
	onMount (() => {
		
	})
*/


let value = ""


</script>



<div 
	class="card variant-soft-primary p-1" 
	style="
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
		grid-template-rows: auto;
		gap: 0.1cm;
		
		color: inherit
	"
>		
	<span 
		class="badge variant-soft-primary"
		style="
			word-wrap: revert-layer;
			white-space: preserve;
		"
	>{ logo }</span>
	
	<label 
		class="label"
		style="display: flex; align-items: center;"
	>
		<input 
			monitor="field"
		
			bind:value={ value }
			type="number" 
			
			class="input"
			style="
				text-indent: 10px; 
				padding: 0.1cm;
				padding-right: 0.3cm;
			" 
			
			placeholder="" 
		/>
	</label>
</div>