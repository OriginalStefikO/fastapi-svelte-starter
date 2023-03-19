<script>
  let rand = -1;
  function getRand() {
    fetch("../rand")
      .then(d => d.text())
      .then(d => (rand = parseInt(d)));
  }
</script>

<main>
  <h1>Hello {rand}!</h1>
  <button on:click={getRand}>Get a random number</button>
</main>