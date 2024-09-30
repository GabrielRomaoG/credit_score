<script lang="ts">
	import { page } from '$app/stores';

	export let title: string = '';
	export let path: string = '/';

	let active: boolean;
	$: active = $page.url.pathname === path;
</script>

<a
	class={`rounded-full px-5 py-2 text-center outline outline-1 outline-slate-100 hover:bg-slate-100/20 hover:outline-2 focus:outline-2 ${active && 'bg-slate-100/20'}`}
	href={path}
>
	{title}
</a>
