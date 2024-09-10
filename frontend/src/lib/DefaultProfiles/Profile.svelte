<script lang="ts">
	export let imageUrl: string = 'https://via.placeholder.com/64';
	export let title: string = 'Default Text';
</script>

<div class="flex w-24 flex-col items-center">
	<img src={imageUrl} alt="" class="h-16 w-16 rounded-full object-cover" />
	<p class="mt-1 text-center text-sm text-gray-700">{title}</p>
</div>
