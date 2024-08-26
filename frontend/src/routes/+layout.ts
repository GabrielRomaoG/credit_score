import { i18nObject } from '$i18n/i18n-util';
import { loadLocaleAsync } from '$i18n/i18n-util.async';

export const load = async ({ data: { locale } }) => {
	await loadLocaleAsync(locale);
	i18nObject(locale);

	return { locale };
};
