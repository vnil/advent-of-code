const fs = require('fs');

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n')

    //console.log(findChecksum(arr));
    console.log(findId(arr));
});


function findId(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let k = i + 1; k < arr.length; k++) {
            if (isMatch(arr[i], arr[k])) {
                return chopIt(arr[i], arr[k])
            }
        }
    }
}

function chopIt(str1, str2) {
    console.log(str1, str2);
    const arr1 = str1.split('');
    const arr2 = str2.split('');

    return arr1.reduce((acc, val, i) => {
        if (val === arr2[i]) {
            return acc + val;
        } else {
            return acc;
        }
    }, '')
}

function isMatch(str1, str2) {
    let missCount = 0;
    for (let i = 0; i < str1.length; i++) {
        if (str1.charAt(i) !== str2.charAt(i)) {
            missCount++;
            if (missCount > 1) {
                return false;
            }
        }
    }

    if (missCount === 0) {
        console.log('Totally identical? o_O');
    }

    return true;
}





function findChecksum(arr) {
    const kewl = arr.map(val => {
        return getScanObject(val);
    }).reduce((acc, val) => {
        return {two: acc.two + (val.hasTwo ? 1 : 0), three: acc.three + (val.hasThree ? 1 : 0)};
    }, {two: 0, three: 0});
}

function getScanObject(str) {
    hasTwo = false;
    hasThree = false;
    const orderedLetters = str.split('').sort();

    let lastLetter = '';
    let count = 1;
    for (let i = 0; i < orderedLetters.length; i++) {
        const letter = orderedLetters[i];
        if (letter === lastLetter) {
            count++;
        } else {
            if (count == 3) {
                hasThree = true;
            } else if (count == 2) {
                hasTwo = true;
            }
            count = 1;
        }
        if (hasTwo && hasThree) {
            break;
        }
        lastLetter = orderedLetters[i];
    }
    if (count == 3) {
        hasThree = true;
    } else if (count == 2) {
        hasTwo = true;
    }

    return {
        hasTwo,
        hasThree,
    }
}