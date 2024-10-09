<script lang="ts">
	import Footer from '$lib/Footer/Footer.svelte';
	import Header from '$lib/Header/Header.svelte';
	import { setLocale } from '$i18n/i18n-svelte';
	import '../app.css';
	import Toaster from '$lib/Toaster/Toaster.svelte';

	export let data;
	setLocale(data.locale);
</script>

<Toaster />

<Header />
<slot />
<Footer />
