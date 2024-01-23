<script>
	import Navbar from '$lib/components/Navbar.svelte';
	import './styles.css';

	import linkedin_logo from '$lib/images/logo_linkedin.png';
  import github_logo from '$lib/images/github.svg';
	import instagram_logo from '$lib/images/logo_instagram.png';
</script>

<div class="min-h-screen flex flex-col justify-between items-center box-border">
	<div class="w-full flex flex-col items-center">
		<Navbar />
		
		<main class="max-w-screen-lg p-3 py-2">
			<slot />
		</main>
	</div>

	<footer class="p-3 flex gap-2 items-center">
		<p>Example by <a href="https://www.linkedin.com/in/steffan-ondrej/">Ondřej Šteffan</a></p>
		<a href="https://www.linkedin.com/in/steffan-ondrej/" target="_blank" class="flex items-center justify-center">
			<img class="size-6 object-contain " src={linkedin_logo} alt="Linkedin logo" />
		</a>
		<a href="https://github.com/OriginalStefikO" target="_blank" class="flex items-center justify-center">
			<img class="size-7 mb-0.5 object-contain " src={github_logo} alt="Github logo" />
		</a>
		<a href="https://www.instagram.com/stefik_o/" target="_blank" class="flex items-center justify-center">
			<img class="size-6 object-contain " src={instagram_logo} alt="Instagram logo" />
		</a>
	</footer>
</div>