<script lang="ts">
	import Speedometer from 'svelte-speedometer';
	export let score: number = -1;
</script>

<div class="flex flex-col items-center">
	<Speedometer
		height={175}
		minValue={250}
		maxValue={900}
		value={score}
		currentValueText=""
		customSegmentStops={[250, 466, 684, 900]}
		segmentColors={['#EE6B6B', '#F4E347', '#8ED731']}
		customSegmentLabels={[
			{ text: 'Low', position: 'OUTSIDE', color: '#EE6B6B' },
			{ text: 'Average', position: 'OUTSIDE', color: '#DEA740' },
			{ text: 'High', position: 'OUTSIDE', color: '#75B028' }
		]}
		ringWidth={15}
		needleColor="black"
		needleHeightRatio={0.7}
	/>

	<p class="text-center text-5xl font-bold">{score}</p>
</div>
