const fs = require('fs');
// const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(input => input.split(' '));

// 14
const inputs = `
5 5
*....
..*..
....*
.....
...*.
`.trim().split("\n");

let N, M;
let map;

const deltas = [
  { r: 0, c: 1 },
  { r: 0, c: -1 },
  { r: 1, c: 0 },
  { r: -1, c: 0 },
];

const checkAllTargets = () => {
  let cnt = 0;
  for (let i = 0; i < N; ++i) {
    for (let j = 0; j < M; ++j) {
      if (map[i][j] === '.') ++cnt;
    }
  }

  return cnt;
};

const checkRange = (r, c) => {
  return !(r >= N || c >= M || r < 0 || c < 0);
};

const go = () => {

};

let caseIdx = 1;

for (let i = 0; i < inputs.length; ++i) {
  const line = inputs[i];

  if (!line.startsWith('.') && !line.startsWith('*')) {
    [N, M] = line.split(' ').map(e => +e);
    map = inputs.slice(i + 1, i + N + 1).map(input => input.split(''));
    const cnt = checkAllTargets();
    let min = Infinity;

    for (let i = 0; i < N; ++i) {
      for (let j = 0; j < M; ++j) {
        for (const delta of deltas) {
          if (map[i][j] === '.') {
            // 1개는 시작할 때 셈
            const res = go(i, j, delta, cnt - 1);
            min = Math.min(res, min);
          }
        }
      }
    }

    console.log(`Case ${caseIdx++}: ${min}`);
  }
}