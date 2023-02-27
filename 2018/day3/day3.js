const fs = require('fs');

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n');
    const objects = arr.map(row => parseRow(row));
    //console.log(objects);
    console.log(cutIt(objects));
});

function parseRow(row) {
    const parts = row.split(' ');
    const offsets = parts[2].slice(0, -1).split(',');
    const measures = parts[3].split('x');
    const left = parseInt(offsets[0]);
    const top = parseInt(offsets[1]);
    const width = parseInt(measures[0]);
    const height = parseInt(measures[1]);
    
    return {
        claimId: parts[0].slice(1),
        left,
        top,
        width,
        height,
        right: left + width,
        bottom: top + height
    }
}

function cutIt(claims) {
    const fabric = [];
    const occupiedSquareInches = claims.reduce((acc, claim) => {
        const occupied = doClaimOnFabric(claim, fabric);
        return occupied + acc;
    }, 0)

    const intact = claims.filter((claim) => isFree(claim, fabric));
    console.log(intact);

    return occupiedSquareInches;
}

function isFree(claim, fabric) {
    for (let x = claim.left; x < claim.right; x++) {
        for (let y = claim.top; y < claim.bottom; y++) {
            if (fabric[x][y] !== claim.claimId) {
                return false;
            }
        }
    }

    return true;
}

function doClaimOnFabric(claim, fabric) {
    let inchesOccupied = 0;
    for (let x = claim.left; x < claim.right; x++) {
        if (!fabric[x]) {
            fabric[x] = [];
        }
        for (let y = claim.top; y < claim.bottom; y++) {
            if (fabric[x][y]) {
                if (fabric[x][y] !== 'X') {
                    fabric[x][y] = 'X';
                    inchesOccupied++;
                }
            } else {
                fabric[x][y] = claim.claimId;
            }
        }
    }

    return inchesOccupied;
}