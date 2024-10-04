import type { Education, Sex } from '$lib/enums';

export interface Features {
	age: number;
	monthly_income: number;
	sex: Sex;
	education: Education;
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
	monthly_income: number;
	sex: number;
	education: number;
	num_bank_accounts: number;
	num_credit_card: number;
	num_of_loan: number;
	num_of_delayed_payment: number;
	outstanding_debt: number;
	credit_history_age: number;
	total_emi_per_month: number;
}

export interface PredictOutput {
	credit_score: number;
	features_relevance: FeaturesRelevance;
}

export interface ProfileInfo {
	profile_id: number;
	title: string;
	img_url: string;
}

export interface DefaultProfiles {
	profiles: ProfileInfo[];
}

export interface Profile {
	profile_info: ProfileInfo;
	features: Features;
	predict_output: PredictOutput;
}
