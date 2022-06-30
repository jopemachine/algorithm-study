const fs = require('fs');
// const [first, ...lines] = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [first, ...lines] = `
2 3
2 7 1
1 9 3
`.trim().split('\n');

const [N, M] = first.split(' ').map(str => Number(str));

const stuffs = [];
for (const line of lines) {
  const [V, C, K] = line.split(' ').map(str => Number(str));
  stuffs.push({
    weight: V,
    like: C,
    count: K,
  });
}

const cache = [];

for (let i = 0; i < N; ++i) {
  cache[i] = [];
  for (let j = 0; j < M; ++j) {
    cache[i][j] = [];
    for (let k = 0; k < stuffs[i].count; ++k) {
      cache[i][j][k] = 0;
    }
  }
}

// idx 이후의 물건들로 구성할 수 있는 최대 만족도
// => idx 물건을 몇 개까지 챙기냐
const pack = (idx = 0, remaining = M, cnt = 0) => {
  let max = 0;
  if (idx === N) return;

  if (cache[idx][remaining][cnt]) return cache[idx][remaining][cnt];

  // 물건을 k개 까지 담는 경우
  for (let k = 0; k < stuffs[idx].count; ++k) {
    // 가방 용량이 충분하다면
    if (remaining - stuffs[idx].weight * k >= 0) {
      const cand = cache[idx][remaining][k] ? cache[idx][remaining][k] :
        pack(idx + 1, remaining - stuffs[idx].weight * k);

      max = Math.max(cand, max);
      cache[idx][remaining][k] = max;
    }
  }
};

console.log(pack());