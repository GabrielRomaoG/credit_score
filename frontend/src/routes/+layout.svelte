<script lang="ts">
	import Footer from '$lib/Footer/Footer.svelte';
	import Header from '$lib/Header/Header.svelte';
	import { setLocale } from '$i18n/i18n-svelte';
	import '../app.css';

	export let data;
	setLocale(data.locale);
</script>

<Header />
<slot />
<Footer />
