const { exit } = require('process');

fs = require('fs');
const data = JSON.parse(fs.readFileSync('./data.json', 'utf-8'));
const argDay = process.argv.slice(2)[0];
const limit = process.argv.slice(2)[1];

if (!argDay) {
  console.error('Please provide a day');
  exit(1);
}

const year = 2020;

const leadingZero = (n) => {
  return n < 10 ? '0' + n : '' + n;
};

const printDay = (dayN) => {
  day = leadingZero(dayN);

  compDate = new Date(`${year}-12-${day}T05:00:00.000Z`).getTime();
  let longestName = 0;
  const diff = (ti) => {
    const solved = new Date(ti).getTime();
    return Math.floor((solved - compDate) / 1000);
  };

  const t = Object.keys(data.members).map((id) => {
    const user = data.members[id];
    const times = user.completion_day_level['' + dayN];
    longestName = Math.max(longestName, user.name.length);
    if (times) {
      return {
        name: user.name,
        p1: times['1']
          ? diff(parseInt(times['1'].get_star_ts) * 1000)
          : undefined,
        p2: times['2']
          ? diff(parseInt(times['2'].get_star_ts) * 1000)
          : undefined,
      };
    }
    return {
      name: user.name,
    };
  });

  const parseTime = (t) => {
    if (!t && t !== 0) {
      return '';
    }
    const hours = Math.floor(t / (60 * 60));
    const minutes = Math.floor((t - hours * 60 * 60) / 60);
    const seconds = t - hours * 60 * 60 - minutes * 60;

    return `${leadingZero(hours)}:${leadingZero(minutes)}:${leadingZero(
      seconds
    )}`;
  };

  best1 = t.reduce((acc, a) => {
    return a.p1 ? Math.min(acc, a.p1) : acc;
  }, 99999999);

  const sorted = t.sort((a, b) => {
    if (!a.p2 && !b.p2) {
      return 0;
    }
    if (!a.p2) {
      return 1;
    }
    if (!b.p2) {
      return -1;
    }
    return a.p2 - b.p2;
  });

  limited = limit ? sorted.splice(0, +limit) : sorted;
  limited.forEach(({ name, p1, p2 }) => {
    part1Diff = parseTime(Math.abs(p1 - best1)) || '--:--:--';
    const spaces = [...new Array(longestName - name.length + 2)]
      .fill(' ')
      .join('');
    const padding = [...new Array(3)].fill(' ').join('');
    console.log(
      `${name}${spaces}${parseTime(
        p1
      )}${padding}(${part1Diff})${padding}${parseTime(p2)}`
    );
  });
};

const days = [...new Array(25)].map((_, i) => i + 1);

if (argDay) {
  printDay(argDay);
} else {
  days.forEach((day) => {
    printDay(day);
  });
}
