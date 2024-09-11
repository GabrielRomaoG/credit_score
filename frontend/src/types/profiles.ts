import type { Features, PredictOutput } from './predict';

export interface ProfileInfo {
	profile_id: number;
	title: string;
}

export interface DefaultProfiles {
	profiles: ProfileInfo[];
}

export interface Profile {
	profile_info: ProfileInfo;
	features: Features;
	predict_output: PredictOutput;
}
