<script>
	import Profile from './Profile.svelte';

	export let profiles = [
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 1',
			labelText: 'Jovem Estudante'
		},
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 2',
			labelText: 'Profissional Experiente'
		},
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 3',
			labelText: 'Profissional de meia-idade'
		}
	];
</script>

<div class="max-w-[600px] grow self-center rounded-lg border bg-white p-4 shadow-lg">
	<h2 class="mb-4 text-center text-lg font-semibold">Check Default Profiles</h2>

	<div class="flex justify-between">
		{#each profiles as profile (profile.labelText)}
			<Profile
				imageUrl={profile.imageUrl}
				altText={profile.altText}
				labelText={profile.labelText}
			/>
		{/each}
	</div>
</div>
