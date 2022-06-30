const fs            = require('fs');
// const [n, inputs]   = fs.readFileSync("/dev/stdin")
//                             .toString()
//                             .trim()
//                             .split('\n');
const [n, inputs]   = `
5
3 1 2 4 5
`
                            .trim()
                            .split('\n');

const N             = +n;
const nums          = inputs.split(' ').map(e => +e);

let ans = 0;

const go = () => {
  const que = [];

  que.push({
    energy: 0,
    remaining: nums,
  });

  const cache = [];

  while (que.length > 0) {
    const { energy, remaining } = que.shift();

    // 2개 빼고 다 골랐을 때
    if (remaining.length === 2) {
      ans = Math.max(ans, energy);
      continue;
    }

    for (let i = 1; i < remaining.length - 1; ++i) {
      const nextRemaining = [...remaining];
      nextRemaining.splice(i, 1);

      const key = nextRemaining.join(',') + '@' + energy;

      if (cache[key]) {
        console.log('hit', key);
        continue;
      }

      cache[key] = true;

      que.push({
        energy: energy + (remaining[i - 1] * remaining[i + 1]),
        remaining: nextRemaining,
      });
    }
  }
};

go();

console.log(ans);