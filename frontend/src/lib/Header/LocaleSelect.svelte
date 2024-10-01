<script lang="ts">
	import { browser } from '$app/environment';
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import { setLocale, locale } from '$i18n/i18n-svelte';
	import type { Locales } from '$i18n/i18n-types';
	import { locales } from '$i18n/i18n-util';
	import { loadLocaleAsync } from '$i18n/i18n-util.async';
	import { createSelect, melt } from '@melt-ui/svelte';
	import { ChevronDown } from 'lucide-svelte';
	import { fade } from 'svelte/transition';

	const {
		elements: { trigger, menu, option },
		states: { open, selected }
	} = createSelect<Locales>({
		forceVisible: true,
		positioning: {
			placement: 'bottom',
			fitViewport: true,
			sameWidth: true
		}
	});

	const switchLocale = async (newLocale?: Locales) => {
		if (newLocale === undefined || newLocale === $locale) return;

		await loadLocaleAsync(newLocale as Locales);
		setLocale(newLocale as Locales);

		invalidateAll();
	};

	$: if (browser) {
		document.querySelector('html')!.setAttribute('lang', $locale);
		const lang = $page.params.lang as Locales;
		switchLocale(lang);
	}

	const getLocaleLabel = (locale: Locales): string => {
		const localeLabelMap: Record<Locales, string> = {
			'en-US': 'English/USD',
			'pt-BR': 'Português/R$'
		};

		return localeLabelMap[locale] ?? locale;
	};
</script>

<div>
	<button
		class="flex justify-between gap-1 rounded-full px-4 py-2 text-center outline outline-1 outline-slate-100 transition-all hover:bg-slate-100/20 hover:outline-2 focus:outline-2"
		use:melt={$trigger}
		aria-label="Locale"
	>
		{getLocaleLabel($locale)}
		<ChevronDown />
	</button>
	{#if $open}
		<div
			class="flex flex-col overflow-y-auto rounded-lg bg-white p-1 shadow"
			use:melt={$menu}
			transition:fade={{ duration: 150 }}
		>
			{#each locales as item}
				<button
					class="cursor-pointer rounded-lg px-2 py-1 hover:bg-slate-100"
					use:melt={$option({ value: item, label: getLocaleLabel(item) })}
					on:click={() => switchLocale($selected?.value)}
				>
					{getLocaleLabel(item)}
				</button>
			{/each}
		</div>
	{/if}
</div>
