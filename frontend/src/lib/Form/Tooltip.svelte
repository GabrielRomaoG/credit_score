<script lang="ts">
	import { createTooltip, melt } from '@melt-ui/svelte';
	import { fade } from 'svelte/transition';
	import { MessageCircleMore } from 'lucide-svelte';

	const {
		elements: { trigger, content, arrow },
		states: { open }
	} = createTooltip({
		positioning: {
			placement: 'right'
		},
		openDelay: 0,
		closeDelay: 0,
		closeOnPointerDown: false,
		forceVisible: true
	});

	export let infoMessage: string = '';
	export let iconColor: string = 'text-slate-100';
</script>

<button type="button" use:melt={$trigger} aria-label="Info">
	<MessageCircleMore class="h-6 w-6 pb-1 {iconColor}" />
</button>

{#if $open}
	<div
		use:melt={$content}
		transition:fade={{ duration: 100 }}
		class=" z-10 max-w-64 rounded-lg bg-white shadow"
	>
		<div use:melt={$arrow} />
		<p class="break-words px-4 py-1 text-justify text-sm">{infoMessage}</p>
	</div>
{/if}
