<script>
	// Import the Profile component
	import Profile from './Profile.svelte';

	// Expect an array of profiles to be passed in as a prop
	export let profiles = [
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 1',
			labelText: 'User 1'
		},
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 2',
			labelText: 'User 2'
		},
		{
			imageUrl: 'https://via.placeholder.com/64',
			altText: 'Profile 3',
			labelText: 'User 3'
		}
	];
</script>

<div class="rounded-lg border bg-white p-4 shadow-lg">
	<!-- Static Title -->
	<h2 class="mb-4 text-center text-lg font-semibold">Check Default Profiles</h2>

	<!-- Profiles Container -->
	<div class="flex justify-between space-x-2">
		<!-- Render each profile dynamically -->
		{#each profiles as profile (profile.labelText)}
			<Profile
				imageUrl={profile.imageUrl}
				altText={profile.altText}
				labelText={profile.labelText}
			/>
		{/each}
	</div>
</div>
