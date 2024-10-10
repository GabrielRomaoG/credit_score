<script lang="ts">
	import type { ProfileInfo } from '$lib/types';
	import Profile from './Profile.svelte';
	import { goto } from '$app/navigation';
	import LL from '$i18n/i18n-svelte';

	export let profileSelectedId: number | undefined;

	export let profiles: ProfileInfo[] = [
		{
			profile_id: 1,
			title: 'Jovem Estudante',
			img_url: 'https://via.placeholder.com/64'
		},
		{
			profile_id: 2,
			title: 'Profissional Experiente',
			img_url: 'https://via.placeholder.com/64'
		},
		{
			profile_id: 3,
			title: 'Profissional de meia-idade',
			img_url: 'https://via.placeholder.com/64'
		}
	];

	function handleClick(profile_id: number) {
		goto(`?profile_id=${profile_id}`, { invalidateAll: true }).then(() => {
			window.location.reload();
			document.getElementById('form')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
		});
	}
</script>

<div class="max-w-[600px] grow basis-[300px] rounded-lg border bg-white shadow-lg sm:p-4">
	<h2 class="mb-4 text-center text-lg font-semibold">{$LL.home.check_default_profiles()}</h2>

	<div class="flex content-stretch justify-between">
		{#each profiles as profile (profile.profile_id)}
			<button
				on:click={() => handleClick(profile.profile_id)}
				class={`flex rounded-lg p-2 transition-colors focus:outline-none ${
					profileSelectedId === profile.profile_id ? 'bg-blue-200' : 'hover:bg-gray-200'
				}`}
				disabled={profileSelectedId === profile.profile_id}
			>
				<Profile
					imageUrl={profile.img_url}
					title={profile.title.charAt(0).toUpperCase() + profile.title.slice(1)}
				/>
			</button>
		{/each}
	</div>
</div>
