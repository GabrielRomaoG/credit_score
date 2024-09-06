<script lang="ts">
	import Speedometer from 'svelte-speedometer';
	export let isActive: boolean = false;
	export let score: number = 450;

	// Determine the Speedometer settings based on the score
	let segmentColors: Array<string> = [];
	let customSegmentLabels: Array<{ text: string; position: string; color: string }> = [];
	let minValue = 250;
	let maxValue = 900;

	if (isActive) {
		// Default settings for scores 250 and above
		segmentColors = ['#EE6B6B', '#F4E347', '#8ED731'];
		customSegmentLabels = [
			{ text: 'Low', position: 'OUTSIDE', color: '#EE6B6B' },
			{ text: 'Average', position: 'OUTSIDE', color: '#DEA740' },
			{ text: 'High', position: 'OUTSIDE', color: '#75B028' }
		];
	} else if (!isActive) {
		segmentColors = ['#D3D3D3', '#A9A9A9', '#808080'];
		customSegmentLabels = [
			{ text: '', position: 'OUTSIDE', color: '#808080' },
			{ text: '', position: 'OUTSIDE', color: '#A9A9A9' },
			{ text: '', position: 'OUTSIDE', color: '#D3D3D3' }
		];
		minValue = 0;
		maxValue = 1;
	}
</script>

<div class="flex flex-col items-center">
	<Speedometer
		height={175}
		{minValue}
		{maxValue}
		value={!isActive ? 0 : score}
		currentValueText=""
		customSegmentStops={[
			minValue,
			(maxValue - minValue) / 3 + minValue,
			((maxValue - minValue) * 2) / 3 + minValue,
			maxValue
		]}
		{segmentColors}
		{customSegmentLabels}
		ringWidth={15}
		needleColor="black"
		needleHeightRatio={0.7}
	/>

	{#if isActive}
		<p class="text-center text-5xl font-bold">{score}</p>
	{/if}
</div>
