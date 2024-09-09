import { detectLocale, i18n } from '$i18n/i18n-util';
import { loadAllLocales } from '$i18n/i18n-util.sync';
import type { Handle, RequestEvent } from '@sveltejs/kit';
import { initAcceptLanguageHeaderDetector } from 'typesafe-i18n/detectors';

loadAllLocales();
const L = i18n();

export const handle: Handle = async ({ event, resolve }) => {
	const LL = L[getPreferredLocale(event)];

	// bind locale and translation functions to current request
	event.locals.locale = getPreferredLocale(event);
	event.locals.LL = LL;

	// replace html lang attribute with correct language
	return resolve(event, {
		transformPageChunk: ({ html }) => html.replace('%lang%', getPreferredLocale(event))
	});
};

// detect the preferred language the user has configured in his browser
const getPreferredLocale = ({ request }: RequestEvent) => {
	return detectLocale(initAcceptLanguageHeaderDetector(request));
};
