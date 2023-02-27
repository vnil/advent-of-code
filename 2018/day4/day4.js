const fs = require('fs');

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n');

    const shifts = arr
        .map(row => parseRow(row))
        .sort((s1, s2) => s1.timeStamp - s2.timeStamp);

    // let currentGuard = 0;
    // shifts.reduce((acc, shift) => {
    //     if (shift.guardId !== currentGuard) {
    //         currentGuard = shift.guardId;
    //         const newGuard = {
    //             guardId: currentGuard,

    //         };
    //     }
    // }, [])


    
    let currentGuard = 0;

    const shiftsPerGuard = shifts.reduce((acc, shift) => {
        if (shift.guardId) {
            currentGuard = shift.guardId;
            if (!acc[currentGuard]) {
                acc[currentGuard] = [];
            }
        }

        acc[currentGuard].push(shift);
        return acc;
    }, {});

    let maxMin = 0;
    let sleepyGuard = 0;

    for (key in shiftsPerGuard) {
        const guard = shiftsPerGuard[key];
        let sleeping = false;
        const sleepyMinutes = guard.reduce((acc, shift) => {
            let minutesAsleep = 0;
            if (shift.awake && sleeping) {
                minutesAsleep = shift.timeStamp - acc.prevShift.timeStamp;
            }

            sleeping = !shift.awake;
            return {
                prevShift: shift,
                accMinutes: acc.accMinutes + minutesAsleep
            }
        }, {prevShift: null, accMinutes: 0}).accMinutes;

        if (maxMin < sleepyMinutes) {
            maxMin = sleepyMinutes;
            sleepyGuard = key;
        }
    }

    const sleepyGuardShifts = shiftsPerGuard[sleepyGuard];
    let sleepInfo = getSleepInfo(sleepyGuardShifts);
    

    console.log(sleepyGuard, sleepInfo.minute, '=>', sleepyGuard * sleepInfo.minute);

    //Part two
    const stuff = [];
    for (key in shiftsPerGuard) {
        const info = getSleepInfo(shiftsPerGuard[key]);
        stuff.push({
            ...info,
            guardId: parseInt(key)
        })
    }

    const sorted = stuff.sort((s1, s2) => s1.timesAsleep - s2.timesAsleep);

    const choice = sorted[sorted.length - 1];
    console.log(choice.minute, choice.guardId, '=>', choice.minute * choice.guardId);
    
});

function getSleepInfo(sleepyGuardShifts) {
    let lastShift = null;
    let sleeping = false;
    const clock = sleepyGuardShifts.reduce((acc, shift) => {
        if (sleeping && shift.awake) {
            for (let i = lastShift.minute; i < shift.minute; i++) {
                acc[i] = (acc[i] || 0) + 1;
            }
        }
        sleeping = !shift.awake;
        lastShift = shift;
        return acc;
    }, new Array(60));

    return clock.reduce((acc, timesAsleep, i) => {
        if (timesAsleep > acc.timesAsleep) {
            return {
                timesAsleep: timesAsleep,
                minute: i
            }
        }
        return acc;
    }, {timesAsleep: 0, minute: 0})
}

function parseRow(row) {
    var regExp = /\[([^)]+)\]\s(.+)/g;
    var matches = regExp.exec(row);
    const shift = {
        guardId: (matches[2].match(/([0-9]+)/) || [])[0],
        //timeStr: matches[1],
        minute: parseInt(matches[1].substr(-2, 2)),
        awake: matches[2] !== 'falls asleep',
        command: matches[2],
        timeStamp: (new Date(matches[1])).getTime() / 1000
    }
    return shift;
}