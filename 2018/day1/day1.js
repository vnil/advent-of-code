const fs = require('fs');
 
fs.readFile('day1.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n').map(val => parseInt(val))
    
    console.log(getSum(arr));

    const freqs = getCalculatedFrequencies(arr, 0);
    let found = false;
    let currentOffset = freqs[freqs.length - 1];
    while (!found) {
        const newArr = getCalculatedFrequencies(arr, currentOffset);
        currentOffset = newArr[newArr.length - 1];

        const frequency = newArr.find(val => freqs.indexOf(val) !== -1);
        if (frequency || frequency === 0) {
            found = true;
            console.log('YEP!', frequency);
        }
        
    }
});


function getSum(arr) {
    return arr.reduce((acc, val) => val + acc);
}

function getCalculatedFrequencies(arr, start, hmm) {
    let buff = start;
    const frequencies = arr.map(val => {
        buff = buff + val;
        return buff;
    })
    return frequencies;

}




 
console.log('after calling readFile');