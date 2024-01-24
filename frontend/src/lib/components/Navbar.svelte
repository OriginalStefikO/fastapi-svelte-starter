<script lang="ts">
  import github_logo from '$lib/images/github.svg';
</script>

<header class="sticky top-0 bg-white w-full flex justify-between items-center px-3 border-b-2 h-20 sm:h-16">
  <h1 class="text-xl w-32 min-w-32 sm:w-fit">SvelteKit + FastAPI starter</h1>
  
  <div class="w-fit flex h-full sm:gap-4">
    <nav class="h-full">
      <ul class="flex h-full">
        <li class="h-full w-fit flex items-center hover:bg-gray-100"><a class="p-3" href="/">Home</a></li>
        <li class="h-full w-fit flex items-center hover:bg-gray-100"><a class="p-3" href="/about">About</a></li>
      </ul>
    </nav>

    <a href="https://github.com/OriginalStefikO/fastapi-svelte-starter" target="_blank" class="flex items-center justify-center shrink-0">
      <img class="size-8 object-contain" src={github_logo} alt="Github logo" />
    </a>
  </div>
</header>