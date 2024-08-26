<script lang="ts">
	import DefaultProfiles from '$lib/DefaultProfiles/DefaultProfiles.svelte';
	import LL from '$i18n/i18n-svelte';
</script>

<main class="top-[100vh] flex w-full items-center justify-between px-44 py-8">
	<div class="flex w-full justify-between">
		<div>
			<h1 class="text-6.5xl font-bold">{$LL.credit_score_ai()}</h1>
			<h2 class="text-2xl">
				Let a Machine Learning model guess your credit score.<br /> It only takes 2 minutes.
			</h2>
		</div>
		<DefaultProfiles />
	</div>
</main>
