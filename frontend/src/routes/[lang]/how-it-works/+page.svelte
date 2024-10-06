<script lang="ts">
	import { LL } from '$i18n/i18n-svelte';
	import Title1 from '$lib/Text/Title1.svelte';
	import Title2 from '$lib/Text/Title2.svelte';
	import Title3 from '$lib/Text/Title3.svelte';
	import NormalText from '$lib/Text/NormalText.svelte';

	const profileExample = {
		age: 30,
		sex: 'male',
		education: 'bachelors_degree',
		monthly_income: 2000,
		num_bank_accounts: 1,
		num_credit_card: 1,
		num_of_loan: 3,
		num_of_delayed_payment: 5,
		outstanding_debt: 15000,
		credit_history_age: 4,
		total_emi_per_month: 600
	};

	const cs1ModelPredictOutput = {
		low: 0.7,
		average: 0.2,
		high: 0.1
	};
</script>

<main class="mx-auto flex w-11/12 max-w-6xl flex-col py-8">
	<Title1 text={$LL.how_it_works.title1()} />

	<Title2 text={$LL.how_it_works.title2_goal()} />

	<NormalText text={$LL.how_it_works.goal_text()} />

	<Title2 text={$LL.how_it_works.title2_data()} />

	<NormalText text={$LL.how_it_works.data_text()} />

	<br />

	<pre class="-indent-10">
	{JSON.stringify(profileExample, null, 2)}
	</pre>

	<Title2 text={$LL.how_it_works.title2_api()} />

	<NormalText text={$LL.how_it_works.api_text()} />

	<Title3 text={$LL.how_it_works.title3_first_model()} />

	<NormalText text={$LL.how_it_works.first_model_text1()} />
	<NormalText text={$LL.how_it_works.first_model_text2()} />

	<br />

	<pre class="-indent-10">
	{JSON.stringify(cs1ModelPredictOutput, null, 2)}
	</pre>

	<NormalText text={$LL.how_it_works.first_model_text3()} />
	<NormalText text={$LL.how_it_works.first_model_text4()} />

	<Title3 text={$LL.how_it_works.title3_second_model()} />

	<NormalText text={$LL.how_it_works.second_model_text()} />

	<Title3 text={$LL.how_it_works.title3_transform_class()} />

	<NormalText text={$LL.how_it_works.transform_class_text1()} />
	<NormalText text={$LL.how_it_works.transform_class_text2()} />
	<NormalText text={$LL.how_it_works.transform_class_text3()} />
	<NormalText text={$LL.how_it_works.transform_class_text4()} />
</main>
