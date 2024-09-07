import { error } from '@sveltejs/kit';

const base = 'https://api.realworld.io/api';

async function send({ method, path, data }: { method: string; path: string; data?: object }) {
	const options: RequestInit = { method, headers: {} };

	if (data) {
		options.headers = [['Content-Type', 'application/json']];
		options.body = JSON.stringify(data);
	}

	const response = await fetch(`${base}/${path}`, options);
	if (response.ok || response.status === 422) {
		const text = await response.text();
		return text ? JSON.parse(text) : {};
	}

	error(response.status);
}

export function get(path: string) {
	return send({ method: 'GET', path });
}

export function del(path: string) {
	return send({ method: 'DELETE', path });
}

export function post(path: string, data: object) {
	return send({ method: 'POST', path, data });
}

export function put(path: string, data: object) {
	return send({ method: 'PUT', path, data });
}
