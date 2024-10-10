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
	import brazil_icon from '$lib/assets/flag-icons/brazil.png';
	import usa_icon from '$lib/assets/flag-icons/usa.png';
	import { replaceLocaleInUrl } from '$lib/utils';

	const {
		elements: { trigger, menu, option },
		states: { open }
	} = createSelect<Locales>({
		forceVisible: true,
		positioning: {
			placement: 'bottom',
			fitViewport: true,
			sameWidth: true
		}
	});

	const switchLocale = async (newLocale?: Locales, updateHistoryState = true) => {
		if (newLocale === undefined || newLocale === $locale) return;

		await loadLocaleAsync(newLocale as Locales);
		setLocale(newLocale);

		if (updateHistoryState) {
			history.pushState({ locale: newLocale }, '', replaceLocaleInUrl($page.url, newLocale));
		}

		invalidateAll();
	};

	const handlePopStateEvent = async ({ state }: PopStateEvent) => switchLocale(state.locale, false);

	$: if (browser) {
		document.querySelector('html')!.setAttribute('lang', $locale);
		const lang = $page.params.lang as Locales;
		switchLocale(lang, false);
		history.replaceState(
			{ ...history.state, locale: lang },
			'',
			replaceLocaleInUrl($page.url, lang)
		);
	}

	const getLocaleLabel = (locale: Locales): string => {
		const localeLabelMap: Record<Locales, string> = {
			'en-US': 'English/USD',
			'pt-BR': 'Português/R$'
		};

		return localeLabelMap[locale] ?? locale;
	};

	const getLocaleFlag = (locale: Locales): string => {
		const localeFlagMap: Record<Locales, string> = {
			'en-US': usa_icon,
			'pt-BR': brazil_icon
		};

		return localeFlagMap[locale] ?? '';
	};
</script>

<svelte:window on:popstate={handlePopStateEvent} />

<div>
	<button
		class="flex items-center justify-between gap-2 rounded-full px-4 py-2 text-center outline outline-1 outline-slate-100 transition-all hover:bg-slate-100/20 hover:outline-2 focus:outline-2"
		use:melt={$trigger}
		aria-label="Locale"
	>
		<img src={getLocaleFlag($locale)} alt="flag" class="h-5 w-8" />
		<span class="hidden min-[440px]:inline">{getLocaleLabel($locale)}</span>
		<ChevronDown />
	</button>

	{#if $open}
		<div
			class="flex flex-col overflow-y-auto rounded-lg bg-white p-1 shadow"
			use:melt={$menu}
			transition:fade={{ duration: 150 }}
		>
			{#each locales as item}
				<a
					class="flex cursor-pointer items-center gap-2 rounded-lg px-2 py-1 hover:bg-slate-100"
					use:melt={$option({ value: item, label: getLocaleLabel(item) })}
					href={replaceLocaleInUrl($page.url, item)}
				>
					<img src={getLocaleFlag(item)} alt="flag" class="h-5 w-8" />
					<span class="hidden min-[440px]:inline">{getLocaleLabel(item)}</span>
				</a>
			{/each}
		</div>
	{/if}
</div>
