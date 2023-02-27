<script>
	import Node from './Node.svelte'
	let game = [
		[null, null, null, null, null, null, null, null, null, null, null], 
		['#', '#', 'C', '#', 'A', '#', 'B', '#', 'D', '#', '#'], 
		['#', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#', '#'],
		['#', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#', '#'],
		['#', '#', 'C', '#', 'A', '#', 'D', '#', 'B', '#', '#']
	];
	let selectedSpot = null;
	let cost = {
		A: 1,
		B: 10,
		C: 100,
		D: 1000
	}

	let moves = {
		A: 0,
		B: 0,
		C: 0,
		D: 0
	}

	$: total_cost = Object.keys(moves).reduce((acc, char) => {
		return cost[char]*moves[char] + acc;
	}, 0)

	$: details = Object.keys(moves).map((char) => {
		return char + ': ' + moves[char];
	})

	//let count = 0;

	const history = []

	function handleBack() {
		const {from, to} = history.pop()
		const currentChar = game[to.r][to.c];
		game[to.r][to.c] = null;
		game[from.r][from.c] = currentChar;
		selectedSpot = {r: from.r, c: from.c}
		moves[currentChar] -= 1
		moves = moves
		game = game;
	}

	function handleKeydown(event) {
		if (!selectedSpot) {
			return;
		}
		const currentChar = game[selectedSpot.r][selectedSpot.c];
		if (!cost[currentChar]) {
			return
		}
		let newR = selectedSpot.r
		let newC = selectedSpot.c
		switch (event.key) {
			case 'ArrowUp':
				newR -= 1;
				break;
			case 'ArrowDown':
				newR += 1;
				break;
			case 'ArrowLeft':
				newC -= 1;
				break;
			case 'ArrowRight':
				newC += 1;
				break;
		}
		if (game[newR][newC] == null) {
			history.push({from: {r: selectedSpot.r, c: selectedSpot.c}, to: {r: newR, c: newC}})
			game[selectedSpot.r][selectedSpot.c] = null;
			game[newR][newC] = currentChar;
			selectedSpot = {r: newR, c: newC}
			moves[currentChar] += 1
			moves = moves;
			game = game;
		}
	}

	function handleSelected(r, c) {
		selectedSpot = {r,c};
	}

	window.printHistory = function() {
		console.log(JSON.stringify(history))
	}

</script>

<svelte:window on:keydown={handleKeydown}/>

<main>
	{#each game as row, r}
		<div class="row">
			{#each row as spot, c}
				<Node char={spot} selected={handleSelected} r={r} c={c} selectedSpot={selectedSpot} />
			{/each}
		</div>
	{/each}

	<button on:click={handleBack}>Back</button>

	<div class="count">Cost: {total_cost}</div>
	<div class="details">
		{#each details as detail}
			<div class="detail-row">{detail}</div>
		{/each}
	</div>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
	}
	
	.row {
		display: flex;

	}

	.count {
		margin-top: 20px;
		font-size: 20px;
	}

	button {
		margin-top: 20px;
	}

	.details {
		margin-top: 20px;
	}

	.detail-row {
		margin-top: 2px;
	}
</style>