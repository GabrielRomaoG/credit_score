<script lang="ts">
	import Linkedin from 'lucide-svelte/icons/linkedin';
	import Github from 'lucide-svelte/icons/github';
	import Mail from 'lucide-svelte/icons/mail';

	export let name: string;
	export let email: string;
	export let githubUserName: string;
	export let linkedinUserName: string;
</script>

<div class="flex flex-col gap-2">
	<p class="text-base font-bold">{name}</p>
	<div class="flex gap-2">
		<Mail size={20} color="#f1f5f9" />
		<a class="text-sm" target="_blank" href={`mailto:${email}`}>{email}</a>
	</div>
	<div class="flex gap-2">
		<Github size={20} color="#f1f5f9" />
		<a class="text-sm" target="_blank" href={`https://github.com/${githubUserName}`}
			>{`/${githubUserName}`}</a
		>
	</div>
	<div class="flex gap-2">
		<Linkedin size={20} color="#f1f5f9" />
		<a class="text-sm" target="_blank" href={`https://www.linkedin.com/in/${linkedinUserName}`}>
			{`/${linkedinUserName}`}
		</a>
	</div>
</div>
