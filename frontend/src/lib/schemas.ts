import { z } from 'zod';
import { Education, Sex } from './enums';

export const featuresSchema = z.object({
	features: z.object({
		age: z.number().nonnegative(),
		monthly_income: z.number().nonnegative(),
		sex: z.nativeEnum(Sex),
		education: z.nativeEnum(Education),
		num_bank_accounts: z.number().nonnegative(),
		num_credit_card: z.number().nonnegative(),
		num_of_loan: z.number().nonnegative(),
		num_of_delayed_payment: z.number().nonnegative(),
		outstanding_debt: z.number().nonnegative(),
		credit_history_age: z.number().nonnegative(),
		total_emi_per_month: z.number().nonnegative()
	})
});
