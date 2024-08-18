<script lang="ts">
	import HeaderNavLink from './HeaderNavLink.svelte';
	import LocaleSelect from './LocaleSelect.svelte';
</script>

<header class="bg-blue-975 flex justify-between px-44 py-8 text-slate-100">
	<nav class="flex gap-4">
		<HeaderNavLink title="Home" />
		<HeaderNavLink title="How it works" path="/how-it-works" />
		<HeaderNavLink title="Authors" path="/authors" />
	</nav>
	<LocaleSelect />
</header>
