<script lang="ts">
	import Speedometer from 'svelte-speedometer';
	export let isActive: boolean = false;
	export let score: number = 450;
</script>

<div class="flex flex-col items-center">
	<Speedometer
		height={160}
		width={260}
		minValue={isActive ? 250 : 0}
		maxValue={isActive ? 900 : 1}
		value={isActive ? score : 0}
		currentValueText=" "
		customSegmentStops={[
			isActive ? 250 : 0,
			isActive ? (900 - 250) / 3 + 250 : 0.33,
			isActive ? ((900 - 250) * 2) / 3 + 250 : 0.66,
			isActive ? 900 : 1
		]}
		segmentColors={isActive
			? [
					score >= 250 && score < 466 ? '#EE6B6B' : '#D3D3D3',
					score >= 466 && score < 684 ? '#F4E347' : '#A9A9A9',
					score >= 684 && score <= 900 ? '#8ED731' : '#808080'
				]
			: ['#D3D3D3', '#A9A9A9', '#808080']}
		customSegmentLabels={isActive
			? [
					{ text: score >= 250 && score < 466 ? 'Low' : '', position: 'OUTSIDE', color: '#EE6B6B' },
					{
						text: score >= 466 && score < 684 ? 'Average' : '',
						position: 'OUTSIDE',
						color: '#DEA740'
					},
					{
						text: score >= 684 && score <= 900 ? 'High' : '',
						position: 'OUTSIDE',
						color: '#75B028'
					}
				]
			: [
					{ text: '', position: 'OUTSIDE', color: '#808080' },
					{ text: '', position: 'OUTSIDE', color: '#A9A9A9' },
					{ text: '', position: 'OUTSIDE', color: '#D3D3D3' }
				]}
		ringWidth={15}
		needleColor="black"
		needleHeightRatio={0.7}
		forceRender={true}
	/>

	{#if isActive}
		<p class="text-center text-5xl font-bold">{score}</p>
	{/if}
</div>
