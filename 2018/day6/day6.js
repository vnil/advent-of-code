const fs = require('fs');

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n');
    const coordinates = arr.map(str => str.split(', ').map(str => parseInt(str)))

    const system = coordinates.reduce((acc, coordinate) => {
        if (!acc.min || !acc.max) {
            acc.min = [...coordinate];
            acc.max = [...coordinate];
        }

        if (acc.min[0] > coordinate[0]) {
            acc.min[0] = coordinate[0]
        }

        if (acc.min[1] > coordinate[1]) {
            acc.min[1] = coordinate[1]
        }

        if (acc.max[0] < coordinate[0]) {
            console.log(acc.max[0], coordinate[0]);
            acc.max[0] = coordinate[0]
        }

        if (acc.max[1] < coordinate[1]) {
            acc.max[1] = coordinate[1]
        }

        return acc;
    }, {})

    const width = system.max[0] - system.min[0] + 1;
    const height = system.max[1] - system.min[1] + 1;

    const grid = [...Array(height)].map(i => [...Array(width)].map(k => ''));

    const painted = grid.map((row, y) => {
        return row.map((point, x) => {
            return findClosestCoordinate([x + system.min[0], y + system.min[1]], coordinates)
        })
    })

    const sorted = coordinates
        .map((c, i) => {
            return numberOfLocations(i, painted);
        })
        .map((count, i) => ({count, index: i}))
        .sort((o1, o2) => o1.count - o2.count)

    console.log(sorted[sorted.length - 1]);

    //Part two
    const distanceMap = grid.map((row, y) => {
        return row.map((location, x) => {
            const locationCoordinates = [x + system.min[0], y + system.min[1]];
            return coordinates.reduce((acc, c) => {
                return Math.abs(c[0] - locationCoordinates[0]) + Math.abs(c[1] - locationCoordinates[1]) + acc;
            }, 0)
        })
    });

    const area = distanceMap.reduce((acc, row) => {
        return row.reduce((acc2, location) => acc2 + (location < 10000 ? 1 : 0), 0) + acc;
    }, 0)

    console.log(area);
});

function numberOfLocations(i, painted) {
    return painted.reduce((acc, row) => {
        return acc + row.reduce((acc2, point) => {
            if (point === i) {
                return ++acc2;
            } else {
                return acc2;
            }
        }, 0);
    }, 0);
}

function findClosestCoordinate(point, coordinates) {
    let closest = '';
    coordinates.reduce((acc, c, i) => {
        const distance = Math.abs(point[0] - c[0]) + Math.abs(point[1] - c[1]);
        if (distance < acc) {
            closest = i;
            return distance;
        } else if (distance === acc) {
            closest = '.';
            return distance;
        } else {
            return acc;
        }
    }, 100000000);
    return closest;
}