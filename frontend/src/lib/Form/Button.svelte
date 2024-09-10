<script lang="ts">
	export let backgroundColor: string = 'bg-blue-500';
	export let textColor: string = 'text-white';
	export let borderColor: string = 'border-transparent';
	export let basis: string = 'basis-full'; // Default to full width
	export let label: string = 'Button';
	export let onClick: (event: Event) => void = () => {};
	export let isSubmit: boolean = false;
</script>

<button
	type={isSubmit ? 'submit' : 'button'}
	on:click={onClick}
	class={`rounded-full px-6 py-2 text-base ${backgroundColor} ${textColor} ${borderColor} ${basis} grow border-2`}
>
	{label}
</button>
