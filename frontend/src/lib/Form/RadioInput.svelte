<script lang="ts" context="module">
	type T = Record<string, unknown>;
</script>

<script lang="ts">
	import { type FormPathLeaves } from 'sveltekit-superforms';
	export let form;

	interface RadioOption {
		label: string;
		value: string;
	}
	export let options: Array<RadioOption>;
	export let name: FormPathLeaves<T>;
	export let selectedValue: string = '';
	export let onChange: (value: string) => void = () => {};
	export let basis: string = 'basis-72';
	export let label: string = 'Radio Input';

	function handleChange(event: Event) {
		const value = (event.target as HTMLInputElement).value;
		selectedValue = value;
		onChange(value);
	}
</script>

<fieldset class={`flex grow flex-col sm:flex-row ${basis} justify-start sm:gap-8`}>
	<legend class="mb-1 text-sm font-medium text-slate-100">{label}</legend>
	{#each options as option}
		<div class={`flex items-center`}>
			<input
				type="radio"
				id={option.value}
				{name}
				value={option.value}
				bind:group={$form[name]}
				checked={selectedValue === option.value}
				on:change={handleChange}
				class="mr-1"
			/>
			<label class="text-sm font-medium text-slate-100" for={option.value}>
				{option.label}
			</label>
		</div>
	{/each}
</fieldset>
