<script>
  export let char;
  export let selected;
  export let r;
  export let c;
  export let selectedSpot;

  $: isSelected = selectedSpot && selectedSpot.r == r && selectedSpot.c == c;
  $: bold = char && char != '#';
</script>

<div on:click={() => selected(r, c)} class={isSelected ? 'selected' : ''}>
  <span class={bold ? 'bold' : ''}>
	  {char ?? '.'}
  </span>
</div>

<style>
	div {
    display: flex;
    justify-content: center;
    align-items: center;  
		width: 30px;
    height: 40px;
    border: 1px solid white;
    background-color: #e5e5e5;
    cursor: pointer;
    color: #666;
	}

  .bold {
    font-weight: bold;
    color: #91a;
  }

  .selected {
    background-color: #c8c8c8;
  }
	
</style>