const fs = require('fs');

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const finalPol = startReactor(contents.split(''));
    //console.log(finalPol.length, finalPol.join(''));
    const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');
    const optimal = letters.map(letter => {
        const regExp = new RegExp(letter, 'gi');
        const left = contents.replace(regExp, '');
        return {unit: letter, poly: startReactor(left.split(''))};
    }).reduce((acc, obj) => {
        if (obj.poly.length < acc.poly.length) {
            return obj;
        } else {
            return acc;
        }
    })

    console.log(optimal, optimal.poly.length);
})

function startReactor(pol) {
    let skipOne = false;
    const reducedPol = pol.reduce((acc, letter, i) => {
        const prevLetter = pol[Math.max(i - 1, 0)];
        if (!skipOne && letter.toLowerCase() === prevLetter.toLowerCase() && letter !== prevLetter) {
            skipOne = true;
            return acc.slice(0, -1);
        } else {
            skipOne = false;
            acc.push(letter);
        }
        return acc;
    }, []);

    if (reducedPol.length === pol.length) {
        return reducedPol;
    } else {
        return startReactor(reducedPol);
    }
}