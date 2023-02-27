function forward(item, steps = 1) {
  if (steps === 0) {
    return item;
  }
  return forward(item.next, steps - 1);
}

function backward(item, steps = 1) {
  if (steps === 0) {
    return item;
  }
  return backward(item.prev, steps - 1);
}

function removeItem(item) {
  const prev = item.prev;
  prev.next = item.next;
  item.next.prev = prev;
}

function debugItem(item, d = {}) {
  if (d[item.value]) {
    return;
  }
  if (!item.next) {
    return;
  }
  d[item.value] = true;
  debugItem(item.next, d);
}

function insertAfter(source, value) {
  const item = { next: source.next, prev: source, value };
  source.next.prev = item;
  source.next = item;
  return item;
}

console.time('time');
const playerCount = 416;
const marbleCount = 71975 * 100;

const players = new Array(playerCount).fill(0);
let currentPlayer = -1;

const start = { prev: null, next: null, value: 0 };
start.prev = start;
start.next = start;

let current = start;

for (let i = 1; i < marbleCount + 1; i++) {
  currentPlayer = (currentPlayer + 1) % playerCount;

  if (i % 23 === 0) {
    const nuke = backward(current, 7);
    players[currentPlayer] += i + nuke.value;
    current = nuke.next;
    removeItem(nuke);
    continue;
  }

  const insertNode = forward(current);
  const newItem = insertAfter(insertNode, i);

  current = newItem;
}
console.timeEnd('time');
console.log('--', Math.max(...players));
