<script lang="ts">
	import type { ProfileInfo } from '$lib/types';
	import Profile from './Profile.svelte';
	import { goto } from '$app/navigation';
	import LL from '$i18n/i18n-svelte';

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

<div class="max-w-[600px] grow basis-[300px] rounded-lg border bg-white shadow-lg sm:p-4">
	<h2 class="mb-4 text-center text-lg font-semibold">{$LL.home.check_default_profiles()}</h2>

	<div class="flex content-stretch justify-between">
		{#each profiles as profile (profile.profile_id)}
			<button
				on:click={() =>
					goto(`?profile_id=${profile.profile_id}`, { invalidateAll: true }).then(() => {
						window.location.reload();
					})}
				class="flex rounded-lg p-2 transition-colors hover:bg-gray-200 focus:outline-none"
			>
				<Profile
					imageUrl={'https://via.placeholder.com/64'}
					title={profile.title.charAt(0).toUpperCase() + profile.title.slice(1)}
				/>
			</button>
		{/each}
	</div>
</div>
