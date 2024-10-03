<script lang="ts">
	import AuthorInfo from './AuthorInfo.svelte';
	import ExternalLink from './ExternalLink.svelte';
	import { createSeparator, melt } from '@melt-ui/svelte';
	import LL from '$i18n/i18n-svelte';

	const {
		elements: { root: separator }
	} = createSeparator({
		orientation: 'vertical',
		decorative: true
	});
</script>

<footer class="sticky top-[100vh] flex w-full justify-center bg-blue-975">
	<div
		class="flex w-11/12 max-w-6xl flex-col gap-10 py-8 text-slate-100 sm:items-center md:flex-row md:justify-between"
	>
		<div class="flex flex-col gap-10 sm:flex-row" id="authors-info">
			<AuthorInfo
				name="Gabriel Romão | Data scientist"
				responsibleFor="Machine learning, backend, frontend, design"
				email="gabriel-rgomes@hotmail.com"
				githubUserName="GabrielRomaoG"
				linkedinUserName="gabriel-rgomes"
			/>
			<div use:melt={$separator} class="hidden w-[1px] bg-slate-100 sm:block" />
			<AuthorInfo
				name="Júlia Machado | Fullstack web developer"
				responsibleFor="Frontend, design"
				email="juliaqmachado@gmail.com"
				githubUserName="juliamxx"
				linkedinUserName="juliaamachado"
			/>
		</div>
		<ExternalLink title={$LL.github_link()} url="https://github.com/GabrielRomaoG/credit_score" />
	</div>
</footer>
