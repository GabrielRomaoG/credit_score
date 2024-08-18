<script lang="ts">
	import { page } from '$app/stores';

	export let title: string = '';
	export let path: string = '/';

	let active: boolean;
	$: active = $page.url.pathname === path;
</script>

<a
	class={`rounded-full border border-slate-100 px-5 py-2 ${active && 'bg-slate-100/20'}`}
	href={path}
>
	{title}
</a>
