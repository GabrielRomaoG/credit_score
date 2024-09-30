// This file was auto-generated by 'typesafe-i18n'. Any manual changes will be overwritten.
/* eslint-disable */
import type {
	BaseTranslation as BaseTranslationType,
	LocalizedString,
	RequiredParams
} from 'typesafe-i18n';

export type BaseTranslation = BaseTranslationType;
export type BaseLocale = 'pt-BR';

export type Locales = 'en-US' | 'pt-BR';

export type Translation = RootTranslation;

export type Translations = RootTranslation;

type RootTranslation = {
	/**
	 * S​c​o​r​e​ ​d​e​ ​C​r​é​d​i​t​o​ ​I​A
	 */
	credit_score_ai: string;
	validation: {
		/**
		 * O​ ​c​a​m​p​o​ ​'​{​f​i​e​l​d​}​'​ ​é​ ​o​b​r​i​g​a​t​ó​r​i​o​.
		 * @param {unknown} field
		 */
		required: RequiredParams<'field'>;
		/**
		 * O​ ​c​a​m​p​o​ ​'​{​f​i​e​l​d​}​'​ ​d​e​v​e​ ​s​e​r​ ​p​o​s​i​t​i​v​o​.
		 * @param {unknown} field
		 */
		nonnegative: RequiredParams<'field'>;
	};
	/**
	 * I​d​a​d​e
	 */
	age: string;
	/**
	 * R​e​n​d​a​ ​m​e​n​s​a​l
	 */
	monthly_income: string;
	/**
	 * S​e​x​o
	 */
	sex: string;
	/**
	 * E​s​c​o​l​a​r​i​d​a​d​e
	 */
	education: string;
	/**
	 * Q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​c​o​n​t​a​s​ ​b​a​n​c​á​r​i​a​s
	 */
	num_bank_accounts: string;
	/**
	 * Q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​c​a​r​t​õ​e​s​ ​d​e​ ​c​r​é​d​i​t​o
	 */
	num_credit_card: string;
	/**
	 * Q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​e​m​p​r​é​s​t​i​m​o​s
	 */
	num_of_loan: string;
	/**
	 * Q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​p​a​g​a​m​e​n​t​o​s​ ​a​t​r​a​s​a​d​o​s
	 */
	num_of_delayed_payment: string;
	/**
	 * D​í​v​i​d​a​ ​t​o​t​a​l
	 */
	outstanding_debt: string;
	/**
	 * H​i​s​t​ó​r​i​c​o​ ​d​e​ ​C​r​é​d​i​t​o
	 */
	credit_history_age: string;
	/**
	 * P​a​r​c​e​l​a​ ​d​e​ ​f​i​n​a​n​c​i​a​m​e​n​t​o
	 */
	total_emi_per_month: string;
	how_it_works: {
		/**
		 * C​o​m​o​ ​f​u​n​c​i​o​n​a​?
		 */
		title1: string;
		/**
		 * O​ ​o​b​j​e​t​i​v​o
		 */
		title2_goal: string;
		/**
		 * O​ ​o​b​j​e​t​i​v​o​ ​d​e​s​t​e​ ​p​r​o​j​e​t​o​,​ ​a​l​é​m​ ​d​e​ ​m​o​s​t​r​a​r​ ​a​s​ ​h​a​b​i​l​i​d​a​d​e​s​ ​d​o​s​ ​a​u​t​o​r​e​s​,​ ​é​ ​m​o​s​t​r​a​r​ ​u​m​ ​p​o​u​c​o​ ​c​o​m​o​ ​u​m​ ​m​o​d​e​l​o​ ​d​e​ ​m​a​c​h​i​n​e​ ​l​e​a​r​n​i​n​g​ ​f​u​n​c​i​o​n​a​ ​c​o​m​ ​s​e​u​s​ ​d​a​d​o​s​ ​e​ ​c​o​m​o​ ​e​l​e​ ​g​e​r​a​ ​o​ ​r​e​s​u​l​t​a​d​o​ ​q​u​e​ ​v​o​c​ê​ ​v​i​u​ ​s​e​ ​v​o​c​ê​ ​t​i​v​e​s​s​e​ ​p​r​e​e​n​c​h​i​d​o​ ​o​ ​f​o​r​m​u​l​á​r​i​o​.​ ​A​ ​e​x​p​l​i​c​a​ç​ã​o​ ​a​ ​s​e​g​u​i​r​ ​é​ ​f​e​i​t​a​ ​p​a​r​a​ ​o​ ​p​ú​b​l​i​c​o​ ​e​m​ ​g​e​r​a​l​,​ ​p​o​r​t​a​n​t​o​,​ ​i​g​n​o​r​a​ ​d​e​t​a​l​h​e​s​ ​t​é​c​n​i​c​o​s​ ​p​a​r​a​ ​u​m​a​ ​m​e​l​h​o​r​ ​c​o​m​p​r​e​e​n​s​ã​o​.
		 */
		goal_text: string;
		/**
		 * C​o​m​o​ ​o​s​ ​d​a​d​o​s​ ​s​ã​o​ ​e​n​v​i​a​d​o​s​?
		 */
		title2_data: string;
		/**
		 * Q​u​a​n​d​o​ ​v​o​c​ê​ ​p​r​e​s​s​i​o​n​a​ ​o​ ​b​o​t​ã​o​ ​e​n​v​i​a​r​ ​a​p​ó​s​ ​p​r​e​e​n​c​h​e​r​ ​o​ ​f​o​r​m​u​l​á​r​i​o​,​ ​o​s​ ​d​a​d​o​s​ ​s​ã​o​ ​e​n​v​i​a​d​o​s​ ​p​a​r​a​ ​u​m​a​ ​A​P​I​ ​n​e​s​t​e​ ​f​o​r​m​a​t​o​:
		 */
		data_text: string;
		/**
		 * A​ ​A​P​I
		 */
		title2_api: string;
		/**
		 * A​ ​A​P​I​ ​é​ ​e​s​c​r​i​t​a​ ​e​m​ ​P​y​t​h​o​n​ ​e​ ​t​e​m​ ​a​ ​t​a​r​e​f​a​ ​d​e​ ​r​e​c​e​b​e​r​ ​o​s​ ​d​a​d​o​s​ ​p​a​s​s​a​d​o​s​ ​p​e​l​o​ ​f​r​o​n​t​e​n​d​ ​e​ ​i​n​s​e​r​i​-​l​o​s​ ​n​o​s​ ​m​o​d​e​l​o​s​.
		 */
		api_text: string;
		/**
		 * O​ ​P​r​i​m​e​i​r​o​ ​M​o​d​e​l​o
		 */
		title3_first_model: string;
		/**
		 * O​ ​p​r​i​m​e​i​r​o​ ​m​o​d​e​l​o​ ​p​r​o​c​e​s​s​a​ ​a​s​ ​c​a​r​a​c​t​e​r​í​s​t​i​c​a​s​ ​[​'​s​e​x​o​'​,​ ​'​e​s​c​o​l​a​r​i​d​a​d​e​'​,​ ​'​i​d​a​d​e​'​,​ ​'​r​e​n​d​a​'​]​ ​e​ ​p​r​e​v​ê​ ​s​e​ ​o​ ​s​e​u​ ​s​c​o​r​e​ ​é​ ​'​b​a​i​x​o​'​,​ ​'​m​é​d​i​o​'​ ​o​u​ ​'​a​l​t​o​'​.​ ​O​ ​m​o​t​i​v​o​ ​p​e​l​o​ ​q​u​a​l​ ​o​ ​m​o​d​e​l​o​ ​n​ã​o​ ​p​r​e​v​ê​ ​o​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​e​m​ ​s​i​ ​é​ ​d​e​v​i​d​o​ ​a​o​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​ ​e​m​ ​q​u​e​ ​f​o​i​ ​t​r​e​i​n​a​d​o​.​ ​O​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​ ​n​ã​o​ ​c​o​n​t​é​m​ ​o​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​;​ ​e​l​e​ ​a​p​e​n​a​s​ ​i​n​f​o​r​m​a​ ​s​e​ ​o​ ​s​c​o​r​e​ ​d​e​ ​u​m​a​ ​p​e​s​s​o​a​ ​é​ ​'​b​a​i​x​o​'​,​ ​'​m​é​d​i​o​'​ ​o​u​ ​'​a​l​t​o​'​.​ ​U​m​ ​m​o​d​e​l​o​ ​q​u​e​ ​p​r​e​v​ê​ ​u​m​a​ ​c​l​a​s​s​e​ ​é​ ​c​h​a​m​a​d​o​ ​d​e​ ​c​l​a​s​s​i​f​i​c​a​d​o​r​.
		 */
		first_model_text1: string;
		/**
		 * O​ ​m​o​d​e​l​o​ ​u​t​i​l​i​z​a​d​o​ ​n​e​s​s​e​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​ ​é​ ​a​ ​r​e​g​r​e​s​s​ã​o​ ​l​o​g​í​s​t​i​c​a​.​ ​A​ ​r​e​g​r​e​s​s​ã​o​ ​l​o​g​í​s​t​i​c​a​ ​é​ ​b​a​s​t​a​n​t​e​ ​s​e​m​e​l​h​a​n​t​e​ ​a​ ​u​m​a​ ​e​q​u​a​ç​ã​o​ ​l​i​n​e​a​r​ ​(​y​ ​=​ ​m​x​ ​+​ ​b​)​,​ ​m​a​s​ ​r​e​s​u​l​t​a​ ​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​e​n​t​r​e​ ​0​ ​e​ ​1​,​ ​p​o​r​ ​i​s​s​o​ ​a​ ​s​a​í​d​a​ ​é​ ​u​m​a​ ​p​r​o​b​a​b​i​l​i​d​a​d​e​.​ ​P​o​r​ ​e​x​e​m​p​l​o​,​ ​p​a​r​a​ ​u​m​ ​c​o​n​j​u​n​t​o​ ​e​s​p​e​c​í​f​i​c​o​ ​d​e​ ​c​a​r​a​c​t​e​r​í​s​t​i​c​a​s​,​ ​o​ ​r​e​s​u​l​t​a​d​o​ ​d​o​ ​m​o​d​e​l​o​ ​é​ ​a​ ​p​r​o​b​a​b​i​l​i​d​a​d​e​ ​d​e​ ​o​b​t​e​r​ ​'​b​a​i​x​o​'​,​ ​'​m​é​d​i​o​'​ ​o​u​ ​'​a​l​t​o​'​.
		 */
		first_model_text2: string;
		/**
		 * O​ ​m​o​d​e​l​o​ ​a​l​c​a​n​ç​a​ ​e​s​s​a​s​ ​p​r​o​b​a​b​i​l​i​d​a​d​e​s​ ​c​a​l​c​u​l​a​n​d​o​ ​a​ ​f​r​e​q​u​ê​n​c​i​a​ ​d​e​ ​c​a​d​a​ ​c​l​a​s​s​e​ ​p​a​r​a​ ​a​s​ ​o​b​s​e​r​v​a​ç​õ​e​s​ ​d​o​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​ ​q​u​e​ ​s​ã​o​ ​s​e​m​e​l​h​a​n​t​e​s​ ​à​ ​e​n​t​r​a​d​a​.​ ​P​o​r​ ​e​x​e​m​p​l​o​,​ ​i​m​a​g​i​n​e​ ​q​u​e​ ​v​o​c​ê​ ​t​e​n​h​a​ ​u​m​ ​c​o​n​j​u​n​t​o​ ​e​s​p​e​c​í​f​i​c​o​ ​d​e​ ​c​a​r​a​c​t​e​r​í​s​t​i​c​a​s​,​ ​o​ ​m​o​d​e​l​o​ ​e​n​c​o​n​t​r​a​r​á​ ​o​b​s​e​r​v​a​ç​õ​e​s​ ​(​l​i​n​h​a​s​ ​d​o​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​)​ ​q​u​e​ ​t​e​n​h​a​m​ ​c​a​r​a​c​t​e​r​í​s​t​i​c​a​s​ ​s​e​m​e​l​h​a​n​t​e​s​,​ ​e​ ​c​o​n​t​a​r​á​ ​a​s​ ​a​p​a​r​i​ç​õ​e​s​ ​d​e​ ​c​a​d​a​ ​c​l​a​s​s​e​.​ ​S​e​ ​a​ ​c​l​a​s​s​e​ ​'​b​a​i​x​o​'​ ​a​p​a​r​e​c​e​r​ ​e​m​ ​7​0​%​ ​d​a​s​ ​l​i​n​h​a​s​,​ ​s​u​a​ ​p​r​o​b​a​b​i​l​i​d​a​d​e​ ​s​e​r​á​ ​d​e​ ​7​0​%​,​ ​e​ ​a​s​s​i​m​ ​p​o​r​ ​d​i​a​n​t​e​.
		 */
		first_model_text3: string;
		/**
		 * É​ ​i​m​p​o​r​t​a​n​t​e​ ​d​i​z​e​r​ ​q​u​e​ ​o​ ​m​o​d​e​l​o​ ​n​ã​o​ ​é​ ​1​0​0​%​ ​p​r​e​c​i​s​o​ ​s​e​ ​c​o​m​p​a​r​a​d​o​ ​a​o​ ​p​r​ó​p​r​i​o​ ​c​o​n​j​u​n​t​o​ ​d​e​ ​d​a​d​o​s​,​ ​e​ ​é​ ​a​i​n​d​a​ ​m​e​n​o​s​ ​p​r​e​c​i​s​o​ ​s​e​ ​c​o​m​p​a​r​a​d​o​ ​a​o​ ​m​u​n​d​o​ ​r​e​a​l​.
		 */
		first_model_text4: string;
		/**
		 * O​ ​S​e​g​u​n​d​o​ ​M​o​d​e​l​o
		 */
		title3_second_model: string;
		/**
		 * O​ ​s​e​g​u​n​d​o​ ​m​o​d​e​l​o​ ​f​u​n​c​i​o​n​a​ ​d​e​ ​m​a​n​e​i​r​a​ ​s​e​m​e​l​h​a​n​t​e​ ​a​o​ ​p​r​i​m​e​i​r​o​.​ ​E​l​e​ ​p​r​o​c​e​s​s​a​ ​a​s​ ​c​a​r​a​c​t​e​r​í​s​t​i​c​a​s​ ​[​'​q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​c​o​n​t​a​s​ ​b​a​n​c​á​r​i​a​s​'​,​ ​'​q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​c​a​r​t​õ​e​s​ ​d​e​ ​c​r​é​d​i​t​o​'​,​ ​'​q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​e​m​p​r​é​s​t​i​m​o​s​'​,​ ​'​q​u​a​n​t​i​d​a​d​e​ ​d​e​ ​p​a​g​a​m​e​n​t​o​s​ ​a​t​r​a​s​a​d​o​s​'​,​ ​'​d​í​v​i​d​a​ ​t​o​t​a​l​'​,​ ​'​h​i​s​t​ó​r​i​c​o​ ​d​e​ ​c​r​é​d​i​t​o​'​,​ ​'​p​a​r​c​e​l​a​ ​d​e​ ​f​i​n​a​n​c​i​a​m​e​n​t​o​'​]​ ​e​ ​p​r​e​v​ê​ ​u​m​a​ ​c​l​a​s​s​e​.
		 */
		second_model_text: string;
		/**
		 * C​o​m​o​ ​e​l​e​ ​t​r​a​n​s​f​o​r​m​a​ ​u​m​a​ ​c​l​a​s​s​e​ ​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​?
		 */
		title3_transform_class: string;
		/**
		 * A​m​b​o​s​ ​o​s​ ​m​o​d​e​l​o​s​ ​p​r​e​v​ê​e​m​ ​u​m​a​ ​c​l​a​s​s​e​ ​c​u​j​a​ ​p​r​o​b​a​b​i​l​i​d​a​d​e​ ​é​ ​a​ ​m​a​i​o​r​.​ ​P​o​r​t​a​n​t​o​,​ ​u​m​ ​m​o​d​e​l​o​ ​p​o​d​e​ ​p​r​e​v​e​r​ ​u​m​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​'​b​a​i​x​o​'​ ​e​ ​o​ ​o​u​t​r​o​ ​u​m​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​'​a​l​t​o​'​.
		 */
		transform_class_text1: string;
		/**
		 * C​a​d​a​ ​u​m​a​ ​d​a​s​ ​c​l​a​s​s​e​s​ ​t​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​a​s​s​o​c​i​a​d​o​ ​a​ ​e​l​a​s​.​ ​P​o​r​ ​e​x​e​m​p​l​o​,​ ​a​ ​c​l​a​s​s​e​ ​'​b​a​i​x​o​'​ ​t​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​d​e​ ​3​0​0​,​ ​a​ ​c​l​a​s​s​e​ ​'​m​é​d​i​o​'​ ​t​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​d​e​ ​6​0​0​,​ ​e​ ​a​ ​c​l​a​s​s​e​ ​'​a​l​t​o​'​ ​t​e​m​ ​u​m​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​d​e​ ​9​0​0​.
		 */
		transform_class_text2: string;
		/**
		 * Q​u​a​n​d​o​ ​o​ ​m​o​d​e​l​o​ ​p​r​e​v​ê​ ​u​m​a​ ​c​l​a​s​s​e​,​ ​e​l​e​ ​r​e​t​o​r​n​a​r​á​ ​o​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​a​s​s​o​c​i​a​d​o​ ​a​ ​e​s​s​a​ ​c​l​a​s​s​e​.​ ​M​a​s​ ​c​o​m​o​ ​t​e​m​o​s​ ​d​o​i​s​ ​m​o​d​e​l​o​s​,​ ​e​l​e​ ​r​e​t​o​r​n​a​r​á​ ​a​ ​m​é​d​i​a​ ​p​o​n​d​e​r​a​d​a​ ​d​o​ ​n​ú​m​e​r​o​ ​d​e​ ​s​c​o​r​e​ ​d​e​ ​c​r​é​d​i​t​o​ ​d​o​s​ ​d​o​i​s​ ​m​o​d​e​l​o​s​,​ ​s​e​n​d​o​ ​o​s​ ​p​e​s​o​s​ ​a​ ​p​r​e​c​i​s​ã​o​ ​d​o​s​ ​m​o​d​e​l​o​s​.
		 */
		transform_class_text3: string;
		/**
		 * P​o​r​ ​e​x​e​m​p​l​o​,​ ​s​e​ ​a​ ​p​r​e​c​i​s​ã​o​ ​d​o​ ​p​r​i​m​e​i​r​o​ ​m​o​d​e​l​o​ ​f​o​r​ ​d​e​ ​7​0​%​ ​e​ ​a​ ​p​r​e​c​i​s​ã​o​ ​d​o​ ​s​e​g​u​n​d​o​ ​m​o​d​e​l​o​ ​f​o​r​ ​d​e​ ​8​0​%​,​ ​e​ ​a​s​ ​c​l​a​s​s​e​s​ ​f​o​r​e​m​ ​'​b​a​i​x​o​'​ ​e​ ​'​a​l​t​o​'​,​ ​a​ ​m​é​d​i​a​ ​p​o​n​d​e​r​a​d​a​ ​s​e​r​á​ ​(​(​7​0​%​ ​*​ ​3​0​0​)​ ​+​ ​(​8​0​%​ ​*​ ​9​0​0​)​)​ ​/​ ​(​7​0​%​ ​+​ ​8​0​%​)​ ​=​ ​6​5​0​.
		 */
		transform_class_text4: string;
	};
};

export type TranslationFunctions = {
	/**
	 * Score de Crédito IA
	 */
	credit_score_ai: () => LocalizedString;
	validation: {
		/**
		 * O campo '{field}' é obrigatório.
		 */
		required: (arg: { field: unknown }) => LocalizedString;
		/**
		 * O campo '{field}' deve ser positivo.
		 */
		nonnegative: (arg: { field: unknown }) => LocalizedString;
	};
	/**
	 * Idade
	 */
	age: () => LocalizedString;
	/**
	 * Renda mensal
	 */
	monthly_income: () => LocalizedString;
	/**
	 * Sexo
	 */
	sex: () => LocalizedString;
	/**
	 * Escolaridade
	 */
	education: () => LocalizedString;
	/**
	 * Quantidade de contas bancárias
	 */
	num_bank_accounts: () => LocalizedString;
	/**
	 * Quantidade de cartões de crédito
	 */
	num_credit_card: () => LocalizedString;
	/**
	 * Quantidade de empréstimos
	 */
	num_of_loan: () => LocalizedString;
	/**
	 * Quantidade de pagamentos atrasados
	 */
	num_of_delayed_payment: () => LocalizedString;
	/**
	 * Dívida total
	 */
	outstanding_debt: () => LocalizedString;
	/**
	 * Histórico de Crédito
	 */
	credit_history_age: () => LocalizedString;
	/**
	 * Parcela de financiamento
	 */
	total_emi_per_month: () => LocalizedString;
	how_it_works: {
		/**
		 * Como funciona?
		 */
		title1: () => LocalizedString;
		/**
		 * O objetivo
		 */
		title2_goal: () => LocalizedString;
		/**
		 * O objetivo deste projeto, além de mostrar as habilidades dos autores, é mostrar um pouco como um modelo de machine learning funciona com seus dados e como ele gera o resultado que você viu se você tivesse preenchido o formulário. A explicação a seguir é feita para o público em geral, portanto, ignora detalhes técnicos para uma melhor compreensão.
		 */
		goal_text: () => LocalizedString;
		/**
		 * Como os dados são enviados?
		 */
		title2_data: () => LocalizedString;
		/**
		 * Quando você pressiona o botão enviar após preencher o formulário, os dados são enviados para uma API neste formato:
		 */
		data_text: () => LocalizedString;
		/**
		 * A API
		 */
		title2_api: () => LocalizedString;
		/**
		 * A API é escrita em Python e tem a tarefa de receber os dados passados pelo frontend e inseri-los nos modelos.
		 */
		api_text: () => LocalizedString;
		/**
		 * O Primeiro Modelo
		 */
		title3_first_model: () => LocalizedString;
		/**
		 * O primeiro modelo processa as características ['sexo', 'escolaridade', 'idade', 'renda'] e prevê se o seu score é 'baixo', 'médio' ou 'alto'. O motivo pelo qual o modelo não prevê o score de crédito em si é devido ao conjunto de dados em que foi treinado. O conjunto de dados não contém o score de crédito; ele apenas informa se o score de uma pessoa é 'baixo', 'médio' ou 'alto'. Um modelo que prevê uma classe é chamado de classificador.
		 */
		first_model_text1: () => LocalizedString;
		/**
		 * O modelo utilizado nesse conjunto de dados é a regressão logística. A regressão logística é bastante semelhante a uma equação linear (y = mx + b), mas resulta em um número entre 0 e 1, por isso a saída é uma probabilidade. Por exemplo, para um conjunto específico de características, o resultado do modelo é a probabilidade de obter 'baixo', 'médio' ou 'alto'.
		 */
		first_model_text2: () => LocalizedString;
		/**
		 * O modelo alcança essas probabilidades calculando a frequência de cada classe para as observações do conjunto de dados que são semelhantes à entrada. Por exemplo, imagine que você tenha um conjunto específico de características, o modelo encontrará observações (linhas do conjunto de dados) que tenham características semelhantes, e contará as aparições de cada classe. Se a classe 'baixo' aparecer em 70% das linhas, sua probabilidade será de 70%, e assim por diante.
		 */
		first_model_text3: () => LocalizedString;
		/**
		 * É importante dizer que o modelo não é 100% preciso se comparado ao próprio conjunto de dados, e é ainda menos preciso se comparado ao mundo real.
		 */
		first_model_text4: () => LocalizedString;
		/**
		 * O Segundo Modelo
		 */
		title3_second_model: () => LocalizedString;
		/**
		 * O segundo modelo funciona de maneira semelhante ao primeiro. Ele processa as características ['quantidade de contas bancárias', 'quantidade de cartões de crédito', 'quantidade de empréstimos', 'quantidade de pagamentos atrasados', 'dívida total', 'histórico de crédito', 'parcela de financiamento'] e prevê uma classe.
		 */
		second_model_text: () => LocalizedString;
		/**
		 * Como ele transforma uma classe em um número de score de crédito?
		 */
		title3_transform_class: () => LocalizedString;
		/**
		 * Ambos os modelos prevêem uma classe cuja probabilidade é a maior. Portanto, um modelo pode prever um score de crédito 'baixo' e o outro um score de crédito 'alto'.
		 */
		transform_class_text1: () => LocalizedString;
		/**
		 * Cada uma das classes tem um número de score de crédito associado a elas. Por exemplo, a classe 'baixo' tem um número de score de crédito de 300, a classe 'médio' tem um número de score de crédito de 600, e a classe 'alto' tem um número de score de crédito de 900.
		 */
		transform_class_text2: () => LocalizedString;
		/**
		 * Quando o modelo prevê uma classe, ele retornará o número de score de crédito associado a essa classe. Mas como temos dois modelos, ele retornará a média ponderada do número de score de crédito dos dois modelos, sendo os pesos a precisão dos modelos.
		 */
		transform_class_text3: () => LocalizedString;
		/**
		 * Por exemplo, se a precisão do primeiro modelo for de 70% e a precisão do segundo modelo for de 80%, e as classes forem 'baixo' e 'alto', a média ponderada será ((70% * 300) + (80% * 900)) / (70% + 80%) = 650.
		 */
		transform_class_text4: () => LocalizedString;
	};
};

export type Formatters = {};
