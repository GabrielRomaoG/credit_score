import { z } from 'zod';
import { Education, Sex } from './enums';
import type { TranslationFunctions } from '$i18n/i18n-types';
import type { Features } from './types';

const numericFieldSchema = (fieldName: string, LL: TranslationFunctions) =>
	z
		.number({ message: LL.validation.required({ field: fieldName }) })
		.nonnegative({ message: LL.validation.nonnegative({ field: fieldName }) });

export const featuresSchema = (LL: TranslationFunctions, defaultValues?: Features) =>
	z.object({
		age: numericFieldSchema('Age', LL)
			.gt(0)
			.default(defaultValues?.age ?? ('' as unknown as number)),
		monthly_income: numericFieldSchema('Monthly income', LL).default(
			defaultValues?.monthly_income ?? ('' as unknown as number)
		),
		sex: z.nativeEnum(Sex).default(defaultValues?.sex ?? Sex.Male),
		education: z
			.nativeEnum(Education)
			.default(defaultValues?.education ?? Education.BachelorsDegree),
		num_bank_accounts: numericFieldSchema('Number of bank accounts', LL).default(
			defaultValues?.num_bank_accounts ?? ('' as unknown as number)
		),
		num_credit_card: numericFieldSchema('Number of credit cards', LL).default(
			defaultValues?.num_credit_card ?? ('' as unknown as number)
		),
		num_of_loan: numericFieldSchema('Number of loan', LL).default(
			defaultValues?.num_of_loan ?? ('' as unknown as number)
		),
		num_of_delayed_payment: numericFieldSchema('Number of delayed payment', LL).default(
			defaultValues?.num_of_delayed_payment ?? ('' as unknown as number)
		),
		outstanding_debt: numericFieldSchema('Outstanding debt', LL).default(
			defaultValues?.outstanding_debt ?? ('' as unknown as number)
		),
		credit_history_age: numericFieldSchema('Credit history age', LL).default(
			defaultValues?.credit_history_age ?? ('' as unknown as number)
		),
		total_emi_per_month: numericFieldSchema('Total EMI per month', LL).default(
			defaultValues?.total_emi_per_month ?? ('' as unknown as number)
		)
	});
