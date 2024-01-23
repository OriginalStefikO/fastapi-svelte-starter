<svelte:head>
	<title>About</title>
	<meta name="description" content="About this app" />
</svelte:head>

<script lang="ts">
	import { onMount } from "svelte";

	let article: {
		title: string;
		body: string;
	};
	
	async function getArticle() {
		const res = await fetch(`https://jsonplaceholder.typicode.com/posts/1`);
		const data = await res.json();
		return data;
	}

	onMount(async () => {
		article = await getArticle();
	});
</script>

<div>
	<h1 class="py-3">About this app</h1>

	<p>
		This is an example of how you can combine 
		<a href="https://kit.svelte.dev" target="_blank">SvelteKit</a> 
		with 
		<a href="https://fastapi.tiangolo.com" target="_blank">FastAPI</a> 
		and 
		<a href="https://tailwindcss.com" target="_blank">Tailwindcss</a>.
	</p>
	
	<h2 class="py-3">QuickStart</h2>
	<p>For a quick start, clone <a href="https://github.com/OriginalStefikO/fastapi-svelte-starter" target="_blank">this repository</a> with:</p>
	<pre class="whitespace-normal p-3 bg-gray-100 rounded-lg text-sm sm:text-base">
		<a class="text-gray-600" href="https://github.com/OriginalStefikO/fastapi-svelte-starter" target="_blank">git clone https://github.com/OriginalStefikO/fastapi-svelte-starter.git .</a>
	</pre>
	<p>For the whole tutorial go to README.md</p>

	<p class="text-red-600 pt-3">Fun fact!</p>
	<h2 class="text-xl">This is an example of article fetched with SSG enabled:</h2>
	<div class="p-3 bg-gray-100 text-gray-600 rounded-lg">
		{#if article}
			<p><b>Title:</b> {article.title}</p>
			<p><b>Body:</b> {article.body}</p>
		{/if}
	</div>
	<p>To see how it works, look to <a href="https://github.com/OriginalStefikO/fastapi-svelte-starter/blob/main/frontend/src/routes/about/%2Bpage.svelte" target="_blank">"/frontend/src/routes/about/+page.svelte"</a> file</p>
</div>