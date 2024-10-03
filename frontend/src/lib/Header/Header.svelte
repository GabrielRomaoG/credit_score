<script lang="ts">
	import { Menu, X } from 'lucide-svelte';
	import HeaderNavLink from './HeaderNavLink.svelte';
	import LocaleSelect from './LocaleSelect.svelte';
	import { createCollapsible, melt } from '@melt-ui/svelte';
	import { slide } from 'svelte/transition';
	import LL from '$i18n/i18n-svelte';

	const NAV_LAYOUT_BREAKPOINT: number = 640;
	let windowWidth: number;

	const {
		elements: { root, content, trigger },
		states: { open }
	} = createCollapsible({ forceVisible: true });
</script>

<svelte:window bind:innerWidth={windowWidth} />

<header class="flex justify-center bg-blue-975 py-8 text-slate-100">
	<div class="flex w-11/12 max-w-6xl justify-between">
		<nav class="flex gap-4" use:melt={$root}>
			<button use:melt={$trigger} class="shadow hover:opacity-75 sm:hidden" aria-label="Toggle">
				{#if $open}
					<X />
				{:else}
					<Menu />
				{/if}
			</button>
			{#if $open || windowWidth >= NAV_LAYOUT_BREAKPOINT}
				<div class="flex flex-col gap-2 sm:flex-row sm:gap-4" use:melt={$content} transition:slide>
					<HeaderNavLink title="Home" />
					<HeaderNavLink title={$LL.how_it_works.title1()} path="/how-it-works" />
					<HeaderNavLink title={$LL.authors()} path="#authors-info" />
				</div>
			{/if}
		</nav>
		<LocaleSelect />
	</div>
</header>
