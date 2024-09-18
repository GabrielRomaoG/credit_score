import * as api from '$lib/api.js';
import { featuresSchema } from '$lib/schemas';
import type { DefaultProfiles, PredictOutput } from '$lib/types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms/server';
import { zod } from 'sveltekit-superforms/adapters';
export async function load({ locals }) {
	const form = await superValidate(zod(featuresSchema(locals.LL)));

	const defaultProfiles: DefaultProfiles = await api.get('default-profiles/', locals.locale);

	return { defaultProfiles, form };
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

		const parsed_response = response as PredictOutput;

		return { validationResult, parsed_response };
	}
};
