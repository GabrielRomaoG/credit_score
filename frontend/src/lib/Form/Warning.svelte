<script lang="ts">
	import { AlertCircle } from 'lucide-svelte';

	export let warningText: string = 'This is a warning message';
</script>

<div
	class="flex flex-col items-start rounded-[32.5px] border border-slate-100 bg-[rgba(231,239,225,0.2)] p-4 sm:flex-row sm:items-center"
>
	<div class="mb-2 flex w-full items-center sm:mb-0 sm:w-auto">
		<AlertCircle class="h-6 w-6 text-slate-100" />
		<span class="ml-2 font-semibold text-slate-100 sm:hidden">Warning</span>
	</div>
	<p class="text-left text-slate-100 sm:ml-3 sm:text-left">{warningText}</p>
</div>
