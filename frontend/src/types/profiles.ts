import type { PredictInput, PredictOutput } from './predict';

export interface ProfileInfo {
	profile_id: number;
	title: string;
}

export interface DefaultProfiles {
	profiles: ProfileInfo[];
}

export interface Profile {
	profile_info: ProfileInfo;
	predict_input: PredictInput;
	predict_output: PredictOutput;
}
