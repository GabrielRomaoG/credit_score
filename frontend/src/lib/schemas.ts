import { z } from 'zod';
import { Education, Sex } from './enums';
import type { TranslationFunctions } from '$i18n/i18n-types';

const numericFieldSchema = (fieldName: string, LL: TranslationFunctions) =>
	z
		.number({ message: LL.validation.required({ field: fieldName }) })
		.nonnegative({ message: LL.validation.nonnegative({ field: fieldName }) });

export const featuresSchema = (LL: TranslationFunctions) =>
	z.object({
		age: numericFieldSchema('Age', LL),
		monthly_income: numericFieldSchema('Monthly income', LL),
		sex: z.nativeEnum(Sex),
		education: z.nativeEnum(Education),
		num_bank_accounts: numericFieldSchema('Number of bank accounts', LL),
		num_credit_card: numericFieldSchema('Number of credit cards', LL),
		num_of_loan: numericFieldSchema('Number of loan', LL),
		num_of_delayed_payment: numericFieldSchema('Number of delayed payment', LL),
		outstanding_debt: numericFieldSchema('Outstanding debt', LL),
		credit_history_age: numericFieldSchema('Credit history age', LL),
		total_emi_per_month: numericFieldSchema('Total EMI per month', LL)
	});
