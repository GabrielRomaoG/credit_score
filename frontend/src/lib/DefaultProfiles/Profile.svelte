<script>
	export let imageUrl = 'https://via.placeholder.com/64';
	export let altText = 'Default Alt Text';
	export let labelText = 'Default Text';
</script>

<div class="flex w-24 flex-col items-center justify-center">
	<img src={imageUrl} alt={altText} class="h-16 w-16 rounded-full object-cover" />
	<p class="mt-1 text-center text-sm text-gray-700">{labelText}</p>
</div>
