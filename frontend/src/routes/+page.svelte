<script lang="ts">
	import DefaultProfiles from '$lib/DefaultProfiles/DefaultProfiles.svelte';
	import Warning from '$lib/Form/Warning.svelte';
	import LL from '$i18n/i18n-svelte';
	import NumericInput from '$lib/Form/NumericInput.svelte';
	import Button from '$lib/Form/Button.svelte';
	import RadioInput from '$lib/Form/RadioInput.svelte';
</script>

<main class="flex w-full flex-col items-center justify-center py-8 lg:mx-auto xl:justify-between">
	<div class="mb-10 flex w-11/12 max-w-6xl flex-wrap justify-around gap-10 lg:gap-0">
		<div class="flex grow basis-[600px] flex-col justify-around">
			<h1 class="text-6.5xl font-bold">{$LL.credit_score_ai()}</h1>
			<h2 class="text-2xl">
				Let a Machine Learning model guess your credit score.<br /> It only takes 2 minutes.
			</h2>
		</div>
		<DefaultProfiles />
	</div>

	<div class="flex w-11/12 max-w-6xl flex-wrap">
		<div
			class="grow basis-[621px] bg-blue-975 p-4 max-[980px]:rounded-t-lg min-[981px]:rounded-l-lg"
		>
			<form action="" class="mb-4 flex flex-wrap gap-4">
				<NumericInput label="Age*" />
				<RadioInput label="Gender*" options={['Male', 'Female']} />
				<RadioInput
					label="Education*"
					options={['High School', 'Associates', 'Bachelors', 'Masters', 'Doctorate']}
				/>
				<NumericInput label="Monthly income*" />
				<NumericInput label="Number of bank accounts*" />
				<NumericInput label="Number of credit cards*" />
				<NumericInput label="Number of loans*" />
				<NumericInput label="Number of delayed payments" />
				<NumericInput label="Outstanding debt*" />
				<NumericInput label="Equated Monthly Installment*" />
				<NumericInput label="For how many time do you have a credit card?*" />
			</form>

			<div class="mb-4 flex flex-wrap gap-4">
				<Button
					backgroundColor="bg-transparent"
					textColor="text-slate-100"
					borderColor="border-slate-100"
					label="Reset"
					basis="basis-full sm:basis-1/6"
				/>
				<Button
					backgroundColor="bg-[#6366F1]"
					textColor="text-slate-100"
					borderColor="border-slate-100"
					label="Send"
					basis="basis-full sm:basis-4/6"
				/>
			</div>
			<Warning
				warningText="Este projeto foi construído com o propósito de mostrar o conhecimento dos autores. Não podemos atestar a origem dos dados de treino, portanto não se surpreenda se o resultado diferir da realidade."
			/>
		</div>
		<div class="grow basis-[300px] bg-gray-400 max-[980px]:rounded-b-lg min-[981px]:rounded-r-lg">
			ahh
		</div>
	</div>
</main>
