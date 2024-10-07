import type { Locales } from '$i18n/i18n-types';
import { error } from '@sveltejs/kit';

const base = 'http://0.0.0.0:8000';

async function send({
	method,
	path,
	locale,
	data
}: {
	method: string;
	path: string;
	locale: Locales;
	data?: object;
}) {
	const options: RequestInit = { method, headers: {} };

	options.headers = [['Accept-Language', locale]];

	if (data) {
		options.headers.push(['Content-Type', 'application/json']);
		options.body = JSON.stringify(data);
	}

	const response = await fetch(`${base}/${path}`, options);
	const json = await response.json();
	if (response.ok) {
		return json;
	}

	if (response.status === 422) {
		return { errors: json };
	}

	error(response.status);
}

export function get(path: string, locale: Locales) {
	return send({ method: 'GET', path, locale });
}

export function del(path: string, locale: Locales) {
	return send({ method: 'DELETE', path, locale });
}

export function post(path: string, locale: Locales, data: object) {
	return send({ method: 'POST', path, locale, data });
}

export function put(path: string, locale: Locales, data: object) {
	return send({ method: 'PUT', path, locale, data });
}
