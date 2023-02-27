const getVal = (x, y, sn) => {
  const rackId = x + 10
  const power = rackId * y
  const inc = power + sn
  ko = inc * rackId
  ko = ko % 1000
  if (ko >= 100) {
    return parseInt(ko.toString()[0]) - 5
  } else {
    return -5
  }
}

const serial = 7803;

const arr = [];


for (let y = 0; y < 300; y++) {
  arr[y] = [];
  for (let x = 0; x < 300; x++) {
    arr[y][x] = getVal(x, y, serial);
  } 
}

const ba = []
let max = 0
let maxO = 0
for (let o = 1; o < 300; o++) {
  for (let y = 272; y < 300-o+1; y++) {
    for (let x = 230; x < 300-o+1; x++) {
      let sum = 0
      for (let i = 0; i < o; i++) {
        if (y+i > 300 || sum === -1) {
          sum = -1
          break;
        }
        for (let j = 0; j < o; j++) {
          if (x+j > 300) {
            sum = -1
            break;
          }
          sum+=arr[y+i][x+j]
        }
      }
      if (sum > max) {
        cord = [x, y]
        max = sum;
        maxO = o
      }
    }
  } 
}

console.log(cord, maxO);
