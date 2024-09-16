<script lang="ts">
	import FeatureRelevanceItem from './FeatureRelevanceItem.svelte';

	// Accepting featuresRelevanceList as an object
	export let featuresRelevanceList: { [key: string]: number } = {};
</script>

<ul class="flex flex-col justify-between gap-2">
	{#each Object.entries(featuresRelevanceList) as [name, relevance]}
		<li>
			<FeatureRelevanceItem {name} {relevance} />
		</li>
	{/each}
</ul>
