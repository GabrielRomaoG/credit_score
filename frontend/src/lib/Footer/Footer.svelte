<script lang="ts">
	import AuthorInfo from './AuthorInfo.svelte';
	import ExternalLink from './ExternalLink.svelte';
	import { createSeparator, melt } from '@melt-ui/svelte';

	const {
		elements: { root: vertical }
	} = createSeparator({
		orientation: 'vertical',
		decorative: true
	});
</script>

<footer
	class="bg-blue-975 sticky top-[100vh] flex w-full items-center justify-between px-44 py-8 text-slate-100"
>
	<div class="flex gap-10">
		<AuthorInfo
			name="Gabriel Romão"
			email="gabriel-rgomes@hotmail.com"
			githubUserName="GabrielRomaoG"
			linkedinUserName="gabriel-rgomes"
		/>
		<div use:melt={$vertical} class="w-[1px] bg-slate-100" />
		<AuthorInfo
			name="Júlia Machado"
			email="juliaqmachado@gmail.com"
			githubUserName="juliamxx"
			linkedinUserName="juliaamachado"
		/>
	</div>
	<ExternalLink
		title="Go to GitHub repository"
		url="https://github.com/GabrielRomaoG/credit_score"
	/>
</footer>
