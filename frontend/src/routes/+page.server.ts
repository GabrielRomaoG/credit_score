import * as api from '$lib/api.js';
import { featuresSchema } from '$lib/schemas';
import { fail } from '@sveltejs/kit';
import type { DefaultProfiles } from '../types/profiles';

export async function load({ locals }) {
	const defaultProfiles: DefaultProfiles = await api.get('default-profiles/', locals.locale);

	return { defaultProfiles };
}

export const actions = {
	default: async ({ request, locals }) => {
		const data = await request.formData();

		const features = {
			age: data.get('age'),
			sex: data.get('sex'),
			education: data.get('education'),
			credit_history_age: data.get('credit_history_age'),
			monthly_income: data.get('monthly_income'),
			num_bank_accounts: data.get('num_bank_accounts'),
			num_credit_card: data.get('num_credit_card'),
			num_of_delayed_payment: data.get('num_of_delayed_payment'),
			num_of_loan: data.get('num_of_loan'),
			outstanding_debt: data.get('outstanding_debt'),
			total_emi_per_month: data.get('total_emi_per_month')
		};

		const validationResult = featuresSchema.safeParse(features);

		if (!validationResult.success) {
			fail(422, validationResult.error.format());
		}

		const body = await api.post('predict/', locals.locale, features);

		if (body.errors) {
			return fail(401, body);
		}

		// const value = btoa(JSON.stringify(body.user));
		// cookies.set('jwt', value, { path: '/' });

		// redirect(307, '/');
	}
};
