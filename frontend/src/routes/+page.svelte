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
	import { goto } from '$app/navigation';
	import Title1 from '$lib/Text/Title1.svelte';
	import Tooltip from '$lib/Form/Tooltip.svelte';

	export let data;
	export let form;

	const profileData = data.profileData;
	const profileSelected: boolean = data.profileData !== null;

	const superform = superForm(data.form, {
		validators: zod(featuresSchema($LL)),
		resetForm: false
	});

	function handleReturnHome() {
		goto(`/`, { keepFocus: true, replaceState: true, invalidateAll: true }).then(() => {
			window.location.reload();
		});
	}
</script>

<main class="flex w-full flex-col items-center justify-center py-8 lg:mx-auto xl:justify-between">
	<div class="mb-10 flex w-11/12 max-w-6xl flex-wrap justify-around gap-10 lg:gap-0">
		<div class="flex grow basis-[621px] flex-col justify-around">
			<Title1 text={$LL.home.credit_score_ai()} />
			<h2 class="text-2xl">
				{$LL.home.subtitle.part1()}<br />
				{$LL.home.subtitle.part2()}
			</h2>
		</div>
		<DefaultProfiles
			profiles={data.defaultProfiles.profiles}
			profileSelectedId={profileData?.profile_info?.profile_id}
		/>
	</div>

	<div
		class="flex w-full max-w-6xl flex-wrap rounded-lg shadow-[3.95px_3.95px_5.6px_rgba(0,0,0,0.3)] sm:w-11/12"
	>
		<div
			class="flex grow basis-[621px] flex-col justify-between bg-blue-975 p-4 max-[980px]:rounded-t-lg min-[981px]:rounded-l-lg"
		>
			<form method="POST" use:superform.enhance>
				<div class="mb-4 flex flex-wrap gap-5">
					<NumericInput name="age" label={$LL.age()} {superform} disabled={profileSelected} />
					<RadioInput
						name="sex"
						label={$LL.sex()}
						options={[
							{ label: $LL.female(), value: 'female' },
							{ label: $LL.male(), value: 'male' }
						]}
						selectedValue="male"
						{superform}
					/>
					<RadioInput
						name="education"
						label={$LL.education()}
						options={[
							{ label: $LL.high_school_diploma(), value: 'high_school_diploma' },
							{ label: $LL.associates_degree(), value: 'associates_degree' },
							{ label: $LL.bachelors_degree(), value: 'bachelors_degree' },
							{ label: $LL.masters_degree(), value: 'masters_degree' },
							{ label: $LL.doctorate(), value: 'doctorate' }
						]}
						{superform}
					/>
					/>
					<NumericInput
						name="monthly_income"
						label={$LL.monthly_income()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_bank_accounts"
						label={$LL.num_bank_accounts()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_credit_card"
						label={$LL.num_credit_card()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_of_loan"
						label={$LL.num_of_loan()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="num_of_delayed_payment"
						label={$LL.num_of_delayed_payment()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="outstanding_debt"
						label={$LL.outstanding_debt()}
						{superform}
						disabled={profileSelected}
					/>
					<NumericInput
						name="total_emi_per_month"
						label={$LL.total_emi_per_month()}
						{superform}
						disabled={profileSelected}
						infoMessage={$LL.home.form.total_emi_per_month_info()}
					/>
					<NumericInput
						name="credit_history_age"
						label={$LL.credit_history_age()}
						{superform}
						disabled={profileSelected}
						infoMessage={$LL.home.form.credit_history_age_info()}
					/>
				</div>
				<div class="mb-4 flex flex-wrap gap-4">
					{#if !profileSelected}
						<Button
							onClick={() => superform.reset()}
							backgroundColor="bg-transparent"
							textColor="text-slate-100"
							borderColor="border-slate-100"
							hover="hover:bg-slate-100 hover:text-blue-600 hover:border-blue-600"
							label={$LL.reset()}
							basis="basis-full sm:basis-1/6"
						/>

						<Button
							isSubmit
							backgroundColor="bg-[#6366F1]"
							textColor="text-slate-100"
							borderColor="border-slate-100"
							hover="hover:bg-blue-700 hover:text-white hover:border-blue-900"
							label={$LL.submit()}
							basis="basis-full sm:basis-4/6"
						/>
					{:else}
						<Button
							onClick={handleReturnHome}
							backgroundColor="bg-[#16b56d]"
							textColor="text-slate-100"
							borderColor="border-slate-100"
							hover="hover:bg-green-600 hover:text-white hover:border-green-800"
							label={$LL.return_home()}
							basis="basis-full"
						/>
					{/if}
				</div>
			</form>

			<Warning warningText={$LL.home.warning()} />
		</div>
		<div
			class="grow basis-[300px] bg-slate-50 px-10 py-4 max-[980px]:rounded-b-lg min-[981px]:rounded-r-lg"
		>
			<Score
				isActive={form?.parsedResponse || profileData?.predict_output ? true : false}
				score={form?.parsedResponse?.credit_score || profileData?.predict_output?.credit_score || 0}
			/>

			{#if form?.parsedResponse || profileData?.predict_output ? true : false}
				<div class="flex flex-row gap-4">
					<h2 class="my-4 text-2xl font-bold">{$LL.features_impact()}</h2>
					<Tooltip infoMessage={$LL.home.form.features_impact_info()} iconColor="text-black" />
				</div>
				<FeaturesRelevance
					featuresRelevanceList={form?.parsedResponse?.features_relevance ||
						profileData?.predict_output?.features_relevance}
				/>
			{:else}
				<p class="text-center text-2xl font-bold">{$LL.fill_form()}</p>
			{/if}
		</div>
	</div>
</main>
