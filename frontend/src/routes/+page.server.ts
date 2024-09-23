import * as api from '$lib/api.js';
import { featuresSchema } from '$lib/schemas';
import type { DefaultProfiles, PredictOutput, Profile } from '$lib/types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms/server';
import { zod } from 'sveltekit-superforms/adapters';
export async function load({ url, locals }) {
	const defaultProfiles: DefaultProfiles = await api.get('default-profiles/', locals.locale);

	const profileId = url.searchParams.get('profile_id');
	let profileData: Profile | null = null;

	if (profileId) {
		const response = await api.get(`default-profiles/${profileId}`, locals.locale);

		if (!response || response.errors) {
			throw fail(404, { error: 'Profile not found' });
		}

		profileData = response as Profile;
	}
	const form = await superValidate(zod(featuresSchema(locals.LL, profileData?.features)));

	return {
		defaultProfiles,
		form,
		profileData
	};
}

export const actions = {
	default: async ({ request, locals }) => {
		const validationResult = await superValidate(request, zod(featuresSchema(locals.LL)));

		if (!validationResult.valid) {
			return fail(422, { validationResult });
		}

		const response = await api.post('predict/', locals.locale, validationResult.data);

		if (response.errors) {
			return fail(401, response);
		}

		const parsedResponse = response as PredictOutput;

		return { validationResult, parsedResponse };
	}
};
