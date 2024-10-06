import { base } from '$app/paths';

export const replaceLocaleInUrl = (url: URL, locale: string, full = false): string => {
	const [, , ...rest] = getPathnameWithoutBase(url).split('/');
	const new_pathname = `/${[locale, ...rest].join('/')}`;
	if (!full) {
		return `${new_pathname}${url.search}`;
	}
	const newUrl = new URL(url.toString());
	newUrl.pathname = base + new_pathname;
	return newUrl.toString();
};

const REGEX_START_WITH_BASE = new RegExp(`^${base}`);

export const getPathnameWithoutBase = (url: URL) => url.pathname.replace(REGEX_START_WITH_BASE, '');
