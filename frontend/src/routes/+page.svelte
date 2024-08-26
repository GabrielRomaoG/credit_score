<script lang="ts">
	import DefaultProfiles from '$lib/DefaultProfiles/DefaultProfiles.svelte';
	import LL from '$i18n/i18n-svelte';
</script>

<main
	class="mx-auto flex w-11/12 max-w-6xl items-center justify-center py-8 md:w-4/5 xl:justify-between"
>
	<div class="flex w-full flex-col gap-8 min-[1005px]:flex-row xl:gap-32">
		<div>
			<h1 class="text-6.5xl font-bold">{$LL.credit_score_ai()}</h1>
			<h2 class="text-2xl">
				Let a Machine Learning model guess your credit score.<br /> It only takes 2 minutes.
			</h2>
		</div>
		<DefaultProfiles />
	</div>
</main>
