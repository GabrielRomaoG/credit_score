<script lang="ts">
	export let label: string = 'Numeric Input';
	export let basis: string = 'basis-72';
</script>

<div class={`flex flex-grow ${basis} flex-col items-start`}>
	<!-- svelte-ignore a11y-label-has-associated-control -->
	<label class="mb-1 text-sm font-medium text-slate-100">{label}</label>

	<input
		type="number"
		class="w-full rounded-lg border border-amber-350 bg-slate-100 p-1.5 text-left text-sm focus:border-amber-350 focus:outline-none focus:ring-2 focus:ring-amber-200"
		placeholder="0"
	/>
</div>
