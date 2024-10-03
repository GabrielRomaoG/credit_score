<script lang="ts">
	import Linkedin from 'lucide-svelte/icons/linkedin';
	import Github from 'lucide-svelte/icons/github';
	import Mail from 'lucide-svelte/icons/mail';
	import ExternalLink from './ExternalLink.svelte';

	export let name: string;
	export let responsibleFor: string;
	export let email: string;
	export let githubUserName: string;
	export let linkedinUserName: string;
</script>

<div class="flex flex-col gap-2">
	<p class="text-base font-bold">{name}</p>
	<span>{responsibleFor}</span>
	<div class="flex gap-2">
		<Mail size={20} color="#f1f5f9" />
		<ExternalLink title={email} url={`mailto:${email}`} />
	</div>
	<div class="flex gap-2">
		<Github size={20} color="#f1f5f9" />
		<ExternalLink title={`/${githubUserName}`} url={`https://github.com/${githubUserName}`} />
	</div>
	<div class="flex gap-2">
		<Linkedin size={20} color="#f1f5f9" />
		<ExternalLink
			title={`/${linkedinUserName}`}
			url={`https://www.linkedin.com/in/${linkedinUserName}`}
		/>
	</div>
</div>
