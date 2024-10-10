<script lang="ts" context="module">
	type T = Record<string, unknown>;
</script>

<script lang="ts" generics="T extends Record<string, unknown>">
	import Tooltip from './Tooltip.svelte';

	import { formFieldProxy, type SuperForm, type FormPathLeaves } from 'sveltekit-superforms';
	export let superform: SuperForm<T>;
	export let name: FormPathLeaves<T>;
	export let disabled: boolean = false;
	const { value, errors } = formFieldProxy(superform, name);
	const { validate, isTainted } = superform;

	if (isTainted(name)) {
		validate(name);
	}

	export let infoMessage: string = '';

	export let label: string = 'Numeric Input';
	export let basis: string = 'basis-72';
</script>

<div class={`flex flex-grow ${basis} flex-col items-start`}>
	<!-- svelte-ignore a11y-label-has-associated-control -->
	<div class="mb-1 flex flex-row gap-4">
		<label class=" text-base font-medium text-slate-100 after:content-['*']">{label}</label>
		{#if infoMessage}
			<Tooltip {infoMessage} />
		{/if}
	</div>

	<input
		{disabled}
		{name}
		type="number"
		aria-invalid={$errors ? 'true' : undefined}
		bind:value={$value}
		class="w-full rounded-lg border border-amber-350 bg-slate-100 p-1.5 text-left text-sm focus:border-amber-350 focus:outline-none focus:ring-2 focus:ring-amber-200"
	/>

	{#if $errors}
		<span class="mt-1 text-sm text-red-300">{$errors}</span>
	{/if}
</div>
