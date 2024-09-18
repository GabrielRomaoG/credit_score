import type { Translation } from '../i18n-types';

const en_US = {
	credit_score_ai: 'Credit Score AI',
	validation: {
		required: "'{field}' is required.",
		nonnegative: "'{field}' must be positive."
	},
	age: 'Age',
	monthly_income: 'Monthly Income',
	sex: 'Sex',
	education: 'Education',
	num_bank_accounts: 'Number of Bank Accounts',
	num_credit_card: 'Number of Credit Cards',
	num_of_loan: 'Number of Loans',
	num_of_delayed_payment: 'Number of Delayed Payments',
	outstanding_debt: 'Outstanding Debt',
	credit_history_age: 'Credit History Age',
	total_emi_per_month: 'Total EMI per Month'
} satisfies Translation;

export default en_US;
