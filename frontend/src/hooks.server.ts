import { base } from '$app/paths';
import type { Locales } from '$i18n/i18n-types';
import { detectLocale, i18n, isLocale } from '$i18n/i18n-util';
import { loadAllLocales } from '$i18n/i18n-util.sync';
import { getPathnameWithoutBase } from '$lib/utils';
import { redirect, type Handle, type RequestEvent } from '@sveltejs/kit';
import { initAcceptLanguageHeaderDetector } from 'typesafe-i18n/detectors';

loadAllLocales();
const L = i18n();

export const handle: Handle = async ({ event, resolve }) => {
	const [, lang] = getPathnameWithoutBase(event.url).split('/');

	if (!lang) {
		const locale = getPreferredLocale(event);

		throw redirect(307, `${base}/${locale}`);
	}

	const locale = isLocale(lang) ? (lang as Locales) : getPreferredLocale(event);
	const LL = L[locale];

	event.locals.locale = locale;
	event.locals.LL = LL;

	return resolve(event, {
		transformPageChunk: ({ html }) => html.replace('%lang%', getPreferredLocale(event))
	});
};

const getPreferredLocale = ({ request }: RequestEvent) => {
	return detectLocale(initAcceptLanguageHeaderDetector(request));
};
