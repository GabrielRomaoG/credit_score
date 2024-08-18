<script lang="ts">
	export let title: string;
	export let url: string;
</script>

<!-- TODO: add external link icon after -->
<a class="break-all text-sm font-bold text-slate-100 underline" href={url} target="_blank">
	{title}
</a>
