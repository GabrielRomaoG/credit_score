<script lang="ts">
	import { ChevronsUp, ChevronsDown, ChevronUp, ChevronDown, Minus } from 'lucide-svelte';

	export let name: string = 'Default Name';
	export let relevance: number = 0;

	function getRelevanceIcon() {
		switch (relevance) {
			case 2:
				return { icon: ChevronsUp, color: 'text-green-500' };
			case 1:
				return { icon: ChevronUp, color: 'text-green-500' };
			case 0:
				return { icon: Minus, color: 'text-yellow-500' };
			case -1:
				return { icon: ChevronDown, color: 'text-red-500' };
			case -2:
				return { icon: ChevronsDown, color: 'text-red-500' };
			default:
				return { icon: null, color: '' };
		}
	}

	const { icon, color } = getRelevanceIcon();
</script>

<div class="flex grow items-center justify-between space-x-2">
	<span class="text-base font-medium">{name}</span>
	<div class={`flex items-center ${color}`}>
		{#if icon}
			<svelte:component this={icon} class="h-5 w-5" />
		{/if}
	</div>
</div>
