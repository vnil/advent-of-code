const fs = require('fs');
const { allowedNodeEnvironmentFlags } = require('process');

const data = [];

fs.readFile('day13.txt', 'utf8', function(err, contents) {

  const arr = contents.split('\n');
  for (let i = 0; i < arr.length; i++) {
    data[i] = [];
    for (let j = 0; j < arr[0].length; j++) {
      data[i][j] = arr[i][j];
    }
  }

  const isPlayer = (character) => {
    switch (character) {
      case '^':
      case 'v':
      case '<':
      case '>':
        return true;
      default:
        return false;
    }
  } 
  const dir = {
    '^': [0, -1],
    'v': [0, 1],
    '<': [-1, 0],
    '>': [1, 0],
  }

  const crossDir = {
    '^': ['<', '^', '>'],
    'v': ['>', 'v', '<'],
    '<': ['v', '<', '^'],
    '>': ['^', '>', 'v'],
  }

  const toStr = (x, y) => `${x},${y}`;

  let turnCount = 0


  const ok = (x, y, bad = '|') => {
    return data[y] && (data[y][x] || '').trim() !== '' && data[y][x] !== bad
  }

  const fix = (x, y) => {
    if (ok(x, y+1, '-') && ok(x, y-1, '-') && ok(x+1, y) && ok(x-1, y)) {
      data[y][x] = '+'
      return;
    }
    if (ok(x+1, y) && ok(x-1, y)) {
      data[y][x] = '-'
      return
    }
    if (ok(x, y-1, '-') && ok(x, y+1, '-')) {
      data[y][x] = '|'
      return
    }
    if ((ok(x, y+1, '-') && ok(x-1, y)) || (ok(x, y-1, '-') && ok(x+1, y))) {
      data[y][x] = '\\'
      return
    }
    if ((ok(x+1, y) && ok(x, y+1, '-')) || (ok(x-1, y) && ok(x, y-1, '-'))) {
      data[y][x] = '/'
      return
    }
    console.error('Should not go here', x, y)
  }

  const printIt = () => {
    for (let y = 0; y < data.length; y++) {
      let s1 = ''
      for (let x = 0; x < data[0].length; x++) {
        s1 += data[y][x];
      }
      console.log(s1);
    }
    console.log('');
  }

  const wtf = {};
  let q = false;
  let r = 0
  while (!q) {
    const done = {};
    if (r>440) {
      printIt();
      console.log(r);
    }
    r++
    for (let y = 0; y < data.length; y++) {
      for (let x = 0; x < data[0].length; x++) {
        if (done[toStr(x, y)]) {
          continue;
        }
        const char = data[y][x];
        if (isPlayer(char)) {
          
          fix(x, y);
          const newX = x + dir[char][0];
          const newY = y + dir[char][1];
          let targetChar = ''
          try {
            targetChar = data[newY][newX];
          } catch (e) {
            printIt();
          }
          if (isPlayer(targetChar)) {
            console.log('BOOM', newX, newY);
            fix(newX, newY);
            q = true
            delete wtf[toStr(x, y)];
            continue
          }
          let turnCount = wtf[toStr(x, y)] || 0;
          if (targetChar === '+') {
            const d = crossDir[char][turnCount%3]
            

            data[newY][newX] = d;
            turnCount += 1
          }
          else if (targetChar === '\\') {
            if (char === 'v' || char === '^') {
              data[newY][newX] = crossDir[char][0]
            } else {
              data[newY][newX] = crossDir[char][2]
            }
          }
          else if (targetChar === '/') {
            if (char === 'v' || char === '^') {
              data[newY][newX] = crossDir[char][2]
            } else {
              data[newY][newX] = crossDir[char][0]
            }
          }
          else {
            data[newY][newX] = char;
          }
          delete wtf[toStr(x, y)];
          done[toStr(newX, newY)] = true;
          wtf[toStr(newX, newY)] = turnCount
        }
      }
    }
    if (q) {
      let pc = 0
      for (let y2 = 0; y2 < data.length; y2++) {
        for (let x2 = 0; x2 < data[0].length; x2++) {
          if (isPlayer(data[y2][x2])) {
            pc+=1
          }
        }
      }
      if (pc !== 1) {
        q = false
      }
    }
  }

});


    