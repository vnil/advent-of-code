const fs = require('fs');

let obj = fs
  .readFileSync('./day12.txt')
  .toString()
  .split('\n')
  .map(a => a.trim())
  .map(k => k.split(' => '))
  .reduce((acc, [form, res]) => {
    acc[form] = res;
    return acc;
  }, {});

let initialState =
  '..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#............';

const newPlant = arr => {
  const str = arr.join('');
  if (obj[str]) {
    return obj[str];
  } else {
    return arr[2];
  }
};

const nextState = oldState => {
  const koko = oldState.split('').map((a, i, arr) => {
    return newPlant([
      arr[i - 2] || '.',
      arr[i - 1] || '.',
      arr[i] || '.',
      arr[i + 1] || '.',
      arr[i + 2] || '.'
    ]);
  });
  return '.....' + koko.join('') + '.....';
};

let state = initialState;
const past = [];
let prev = 0;
let diff = 0;
let sum = 0;
console.log(findSum(state));
for (let i = 0; i < 100; i++) {
  state = nextState(state);
  sum = findSum(state, (i + 1) * 5);
  console.log(i, sum, sum - prev);
  diff = sum - prev;
  past.push(sum);
  prev = sum;
}

console.log(sum + (50000000000 - 100) * diff);

function findSum(state, f) {
  const sum = state.split('').reduce((acc, k, i) => {
    if (k === '#') {
      return acc + i - f;
    }
    return acc;
  }, 0);
  return sum;
}
