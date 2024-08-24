<script>
	export let imageUrl = 'https://via.placeholder.com/64'; // Placeholder image URL
	export let altText = 'Default Alt Text'; // Alt text for the image
	export let labelText = 'Default Text'; // Default text below the image
</script>

<div class="flex h-20 w-24 flex-col items-center justify-center rounded-md border bg-white shadow">
	<img src={imageUrl} alt={altText} class="h-16 w-16 rounded-full object-cover" />
	<p class="mt-1 text-center text-sm text-gray-700">{labelText}</p>
</div>
