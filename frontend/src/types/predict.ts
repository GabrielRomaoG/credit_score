import type { Locales } from '$i18n/i18n-types';

export interface Features {
	age: number;
	monthly_income: number;
	sex: 'male' | 'female';
	education:
		| 'bachelors_degree'
		| 'masters_degree'
		| 'doctorate'
		| 'high_school_diploma'
		| 'associates_degree';
	num_bank_accounts: number;
	num_credit_card: number;
	num_of_loan: number;
	num_of_delayed_payment: number;
	outstanding_debt: number;
	credit_history_age: number;
	total_emi_per_month: number;
}

export interface FeaturesRelevance {
	age: number;
	income: number;
	gender: number;
	education: number;
	num_bank_accounts: number;
	num_credit_card: number;
	num_of_loan: number;
	num_of_delayed_payment: number;
	outstanding_debt: number;
	credit_history_age: number;
	total_emi_per_month: number;
}

export interface PredictInput {
	locale: Locales;
	features: Features;
}

export interface PredictOutput {
	credit_score: number;
	features_relevance: FeaturesRelevance;
}
