<script lang="ts">
	export let options: Array<string> = ['Reliability', 'Value', 'Trust', 'Integrity', 'Faith'];
	export let name: string = 'radio-group';
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

<fieldset class={`flex grow ${basis} justify-start gap-8`}>
	<legend class="mb-1 text-sm font-medium text-slate-100">{label}</legend>
	{#each options as option}
		<div class={`flex items-center`}>
			<input
				type="radio"
				id={option}
				{name}
				value={option}
				checked={selectedValue === option}
				on:change={handleChange}
				class="mr-1"
			/>
			<label class="text-sm font-medium text-slate-100" for={option}>
				{option}
			</label>
		</div>
	{/each}
</fieldset>
