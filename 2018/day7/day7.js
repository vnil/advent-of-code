const fs = require('fs');

const alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

fs.readFile('data.txt', 'utf8', function(err, contents) {
    const arr = contents.split('\n');
    const steps = arr.map(str => {
        return {
            req: str.charAt(5),
            step: str.charAt(36)
        }
    })

    const deps = steps.reduce((acc, obj) => {
        if (!acc[obj.step]) {
            acc[obj.step] = [];
        }

        acc[obj.step].push(obj.req);
        return acc;
    }, {})

    const start = steps.filter(item => !steps.find(item2 => item.req === item2.step));
    const startSteps = Array.from(new Set(start.map(it => it.req))).sort()
    startSteps.forEach(step => deps[step] = [])
    stepsCompleted = [];
    stepsInProgress = [];
    let clock = 0;
    function tick() {
        if (Object.keys(deps).length === 0) {
            console.log('-->', stepsCompleted.join(''), clock - 1);
            return;
        }
        finishWorkers();
        const ready = [];
        for (key in deps) {
            if (deps[key].every(step => stepsCompleted.indexOf(step) !== -1) && stepsInProgress.indexOf(key) === -1) {
                ready.push(key);
            }
        }
    
        const availableWorkers = getAvailableWorkers();
        ready.sort().forEach((red, i) => {
            if (availableWorkers[i]) {
                availableWorkers[i].currentStep = red;
                availableWorkers[i].started = clock;
                stepsInProgress.push(red);
            }
        });

        clock++;
        tick();
    }

    function finishWorkers() {
        workers.filter(worker => worker.currentStep).forEach(worker => {
            if (worker.started + 60 + alpha.indexOf(worker.currentStep) + 1 <= clock) {
                stepsCompleted.push(worker.currentStep);
                delete deps[worker.currentStep];
                worker.currentStep = null;
                worker.started = null;
            }
        })
    }

    tick();
})

function StepWorker(id) {
    return {
        workerId: id,
        currentStep: null,
        started: null
    }   
}

const workers = [...Array(5)].map((a, i) => StepWorker(i + 1))
function getAvailableWorkers() {
    return workers.filter(w => !w.currentStep);
}