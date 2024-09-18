<script lang="ts">
	import LL from '$i18n/i18n-svelte';
	import type { FeaturesRelevance } from '$lib/types';
	import FeatureRelevanceItem from './FeatureRelevanceItem.svelte';

	export let featuresRelevanceList: FeaturesRelevance = {
		age: 0,
		sex: 0,
		education: 0,
		monthly_income: 0,
		num_bank_accounts: 0,
		num_credit_card: 0,
		num_of_loan: 0,
		num_of_delayed_payment: 0,
		total_emi_per_month: 0,
		outstanding_debt: 0,
		credit_history_age: 0
	};
</script>

<ul class="flex flex-col justify-between gap-2">
	<li>
		<FeatureRelevanceItem name={$LL['age']()} relevance={featuresRelevanceList.age} />
	</li>
	<li>
		<FeatureRelevanceItem name={$LL['sex']()} relevance={featuresRelevanceList.sex} />
	</li>
	<li>
		<FeatureRelevanceItem name={$LL['education']()} relevance={featuresRelevanceList.education} />
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['monthly_income']()}
			relevance={featuresRelevanceList.monthly_income}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['num_bank_accounts']()}
			relevance={featuresRelevanceList.num_bank_accounts}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['num_credit_card']()}
			relevance={featuresRelevanceList.num_credit_card}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['num_of_loan']()}
			relevance={featuresRelevanceList.num_of_loan}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['num_of_delayed_payment']()}
			relevance={featuresRelevanceList.num_of_delayed_payment}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['outstanding_debt']()}
			relevance={featuresRelevanceList.outstanding_debt}
		/>
	</li>
	<li>
		<FeatureRelevanceItem
			name={$LL['credit_history_age']()}
			relevance={featuresRelevanceList.credit_history_age}
		/>
	</li>
</ul>
