<script lang="ts">
	import type { ProfileInfo } from '$lib/types';
	import Profile from './Profile.svelte';
	import { goto } from '$app/navigation';

	export let profiles: ProfileInfo[] = [
		{
			profile_id: 1,
			title: 'Jovem Estudante'
		},
		{
			profile_id: 2,
			title: 'Profissional Experiente'
		},
		{
			profile_id: 3,
			title: 'Profissional de meia-idade'
		}
	];
</script>

<div class="max-w-[600px] grow basis-[300px] rounded-lg border bg-white p-4 shadow-lg">
	<h2 class="mb-4 text-center text-lg font-semibold">Check Default Profiles</h2>

	<div class="flex justify-between">
		{#each profiles as profile (profile.profile_id)}
			<button
				on:click={() =>
					goto(`?profile_id=${profile.profile_id}`, { invalidateAll: true }).then(() => {
						window.location.reload();
					})}
				class="focus:outline-none"
			>
				<Profile
					imageUrl={'https://via.placeholder.com/64'}
					title={profile.title.charAt(0).toUpperCase() + profile.title.slice(1)}
				/>
			</button>
		{/each}
	</div>
</div>
