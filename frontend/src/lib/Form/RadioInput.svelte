<script lang="ts" context="module">
	type T = Record<string, unknown>;
</script>

<script lang="ts" generics="T extends Record<string, unknown>">
	import LL from '$i18n/i18n-svelte';
	import type { TranslationFunctions } from '$i18n/i18n-types';

	import { type FormPathLeaves, formFieldProxy } from 'sveltekit-superforms';
	import type { SuperForm } from 'sveltekit-superforms/client';
	export let superform: SuperForm<T>;

	const { form } = superform;

	interface RadioOption {
		label: string;
		value: string;
	}
	export let options: Array<RadioOption>;
	export let name: FormPathLeaves<T>;
	export let selectedValue: string = '';
	export let onChange: (value: string) => void = () => {};
	export let basis: string = 'basis-72';
	export let label: string = 'Radio Input';

	const { errors } = formFieldProxy(superform, name);

	function handleChange(event: Event) {
		const value = (event.target as HTMLInputElement).value;
		selectedValue = value;
		onChange(value);
	}
	function getErrorMessage(errors: string[], LL: TranslationFunctions) {
		if (errors[0].includes('Invalid enum value') && errors[0].includes("received ''")) {
			return LL.validation.required({ field: label });
		}

		return errors ?? null;
	}
</script>

<div class={`flex flex-grow ${basis} flex-col items-start`}>
	<fieldset class={`flex grow flex-col justify-start sm:flex-row sm:gap-8`}>
		<legend class="mb-1 text-base font-medium text-slate-100 after:content-['*']">{label}</legend>
		{#each options as option}
			<div class={`flex items-center`}>
				<input
					type="radio"
					id={option.value}
					{name}
					value={option.value}
					bind:group={$form[name]}
					checked={selectedValue === option.value}
					on:change={handleChange}
					class="mr-1"
				/>
				<label class="text-sm font-medium text-slate-100" for={option.value}>
					{option.label}
				</label>
			</div>
		{/each}
	</fieldset>
	{#if $errors}
		<span class="mt-1 text-sm text-red-300">{getErrorMessage($errors, $LL)}</span>
	{/if}
</div>
