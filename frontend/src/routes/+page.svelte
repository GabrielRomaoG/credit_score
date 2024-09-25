<script lang="ts">
	import DefaultProfiles from '$lib/DefaultProfiles/DefaultProfiles.svelte';
	import Warning from '$lib/Form/Warning.svelte';
	import LL from '$i18n/i18n-svelte';
	import NumericInput from '$lib/Form/NumericInput.svelte';
	import Button from '$lib/Form/Button.svelte';
	import RadioInput from '$lib/Form/RadioInput.svelte';
	import Score from '$lib/ScorePanel/Score.svelte';
	import { featuresSchema } from '$lib/schemas.js';
	import { superForm } from 'sveltekit-superforms/client';
	import { zod } from 'sveltekit-superforms/adapters';
	import FeaturesRelevance from '$lib/ScorePanel/FeaturesRelevance.svelte';

	export let data;
	export let form;

	const profileData = data.profileData;
	const profileSelected: boolean = data.profileData !== null;

	const superform = superForm(data.form, {
		validators: zod(featuresSchema($LL)),
		resetForm: false
	});
</script>

<main class="flex w-full flex-col items-center justify-center py-8 lg:mx-auto xl:justify-between">
	<div class="mb-10 flex w-11/12 max-w-6xl flex-wrap justify-around gap-10 lg:gap-0">
		<div class="flex grow basis-[621px] flex-col justify-around">
			<h1 class="text-6.5xl font-bold">{$LL.credit_score_ai()}</h1>
			<h2 class="text-2xl">
				Let a Machine Learning model guess your credit score.<br /> It only takes 2 minutes.
			</h2>
		</div>
		<DefaultProfiles profiles={data.defaultProfiles.profiles} />
	</div>

	<div
		class="flex w-full max-w-6xl flex-wrap rounded-lg shadow-[3.95px_3.95px_5.6px_rgba(0,0,0,0.3)] sm:w-11/12"
	>
		<div
			class="flex grow basis-[621px] flex-col justify-between bg-blue-975 p-4 max-[980px]:rounded-t-lg min-[981px]:rounded-l-lg"
		>
			<form method="POST" use:superform.enhance>
				<div class="mb-4 flex flex-wrap gap-4">
					<NumericInput name="age" label="Age" {superform} disabled={profileSelected} />
					<RadioInput
						name="sex"
						label="Sex"
						options={[
							{ label: 'Male', value: 'male' },
							{ label: 'Female', value: 'female' }
						]}
						selectedValue="male"
						form={superform.form}
					/>
					<RadioInput
						name="education"
						label="Education"
						options={[
							{ label: 'High School', value: 'high_school_diploma' },
							{ label: 'Associate', value: 'associates_degree' },
							{ label: 'Bachelor', value: 'bachelors_degree' },
							{ label: 'Master', value: 'masters_degree' },
							{ label: 'Doctorate', value: 'doctorate' }
						]}
						form={superform.form}
					/>
					/>
					<NumericInput
						name="monthly_income"
						label="Monthly income"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_bank_accounts"
						label="Number of bank accounts"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_credit_card"
						label="Number of credit cards"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_of_loan"
						label="Number of loans"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_of_delayed_payment"
						label="Number of delayed payments"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="outstanding_debt"
						label="Outstanding debt"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="total_emi_per_month"
						label="Equated Monthly Installment"
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="credit_history_age"
						label="For how many time do you have a credit card?"
						{superform}
						disabled={profileSelected}
					/>
				</div>
				<div class="mb-4 flex flex-wrap gap-4">
					<Button
						backgroundColor="bg-transparent"
						textColor="text-slate-100"
						borderColor="border-slate-100"
						label="Reset"
						basis="basis-full sm:basis-1/6"
					/>
					<Button
						isSubmit
						backgroundColor="bg-[#6366F1]"
						textColor="text-slate-100"
						borderColor="border-slate-100"
						label="Send"
						basis="basis-full sm:basis-4/6"
					/>
				</div>
			</form>

			<Warning
				warningText="Este projeto foi construído com o propósito de mostrar o conhecimento dos autores. Não podemos atestar a origem dos dados de treino, portanto não se surpreenda se o resultado diferir da realidade."
			/>
		</div>
		<div
			class="grow basis-[300px] bg-slate-50 px-10 py-4 max-[980px]:rounded-b-lg min-[981px]:rounded-r-lg"
		>
			<Score
				isActive={form || profileSelected ? true : false}
				score={form?.parsedResponse?.credit_score || profileData?.predict_output?.credit_score || 0}
			/>
			<h2 class="my-4 text-2xl font-bold">Features Relevance</h2>

			<FeaturesRelevance
				featuresRelevanceList={form?.parsedResponse?.features_relevance ||
					profileData?.predict_output?.features_relevance}
			/>
		</div>
	</div>
</main>
