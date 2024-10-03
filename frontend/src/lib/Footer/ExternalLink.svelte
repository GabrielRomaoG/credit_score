<script lang="ts">
	export let title: string;
	export let url: string;
</script>

<a
	class="break-all text-sm font-bold text-slate-100 underline transition-all hover:decoration-2 hover:underline-offset-2"
	href={url}
	target="_blank"
>
	{title}
</a>
