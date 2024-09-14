<script lang="ts">
	import type { ZodNumber } from 'zod';
	export let fieldSchema: ZodNumber;
	export let label: string = 'Numeric Input';
	export let basis: string = 'basis-72';
	export let name: string = 'numeric-input';
	export let error: string | null = null;
	export let value: number = 0;

	function handleBlur() {
		const validation = fieldSchema.safeParse(value);

		if (!validation.success) {
			error = validation.error?.errors[0].message;
		} else {
			error = null;
		}
	}

	function handleInput() {
		const validation = fieldSchema.safeParse(value);
		if (validation.success) {
			error = null;
		}
	}
</script>

<div class={`flex flex-grow ${basis} flex-col items-start`}>
	<!-- svelte-ignore a11y-label-has-associated-control -->
	<label class="mb-1 text-sm font-medium text-slate-100 after:content-['*']">{label}</label>

	<input
		{name}
		type="number"
		bind:value
		on:blur={handleBlur}
		on:input={handleInput}
		class="w-full rounded-lg border border-amber-350 bg-slate-100 p-1.5 text-left text-sm focus:border-amber-350 focus:outline-none focus:ring-2 focus:ring-amber-200"
		placeholder="0"
	/>

	{#if error}
		<p class="mt-1 text-sm text-red-300">{error}</p>
	{/if}
</div>
