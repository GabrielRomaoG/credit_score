import * as api from '$lib/api.js';
import type { DefaultProfiles } from '../types/profiles';

export async function load({ locals }) {
	const defaultProfiles: DefaultProfiles = await api.get('default-profiles/', locals.locale);

	return { defaultProfiles };
}
