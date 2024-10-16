import { z } from 'zod';
import { Education, Sex } from './enums';
import type { TranslationFunctions } from '$i18n/i18n-types';
import type { Features } from './types';

const numericFieldSchema = (
	fieldName: string,
	LL: TranslationFunctions,
	lessThan?: number,
	greaterThan?: number
) =>
	z
		.number({ message: LL.validation.required({ field: fieldName }) })
		.lte(lessThan ?? Infinity, { message: LL.validation.lessThan({ field: fieldName, lessThan }) })
		.nonnegative({ message: LL.validation.nonnegative({ field: fieldName }) })
		.gt(greaterThan ?? -Infinity, {
			message: LL.validation.greaterThan({ field: fieldName, greaterThan })
		});

export const featuresSchema = (LL: TranslationFunctions, defaultValues?: Features) =>
	z.object({
		age: numericFieldSchema(LL.age(), LL, 130, 0).default(
			defaultValues?.age ?? ('' as unknown as number)
		),
		monthly_income: numericFieldSchema(LL.monthly_income(), LL, 1e9).default(
			defaultValues?.monthly_income ?? ('' as unknown as number)
		),
		sex: z.nativeEnum(Sex).default(defaultValues?.sex ?? ('' as Sex)),
		education: z.nativeEnum(Education).default(defaultValues?.education ?? ('' as Education)),
		num_bank_accounts: numericFieldSchema(LL.num_bank_accounts(), LL, 1e3).default(
			defaultValues?.num_bank_accounts ?? ('' as unknown as number)
		),
		num_credit_card: numericFieldSchema(LL.num_credit_card(), LL, 1e3).default(
			defaultValues?.num_credit_card ?? ('' as unknown as number)
		),
		num_of_loan: numericFieldSchema(LL.num_of_loan(), LL, 1e3).default(
			defaultValues?.num_of_loan ?? ('' as unknown as number)
		),
		num_of_delayed_payment: numericFieldSchema(LL.num_of_delayed_payment(), LL, 1e3).default(
			defaultValues?.num_of_delayed_payment ?? ('' as unknown as number)
		),
		outstanding_debt: numericFieldSchema(LL.outstanding_debt(), LL, 1e9).default(
			defaultValues?.outstanding_debt ?? ('' as unknown as number)
		),
		credit_history_age: numericFieldSchema(LL.credit_history_age(), LL, 120).default(
			defaultValues?.credit_history_age ?? ('' as unknown as number)
		),
		total_emi_per_month: numericFieldSchema(LL.total_emi_per_month(), LL, 1e9).default(
			defaultValues?.total_emi_per_month ?? ('' as unknown as number)
		)
	});
