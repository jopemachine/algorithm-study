const readline = require('readline');
const inputs = [];
// const inputs = ['9991'];

readline
  .createInterface(process.stdin, {})
  .on('line', function(line) {
    inputs.push(line.trim());
  }).on('close', function() {
    solve();
  });

const factor = (n) => {
  const res = [];
  let k = 2;

  while (k <= n) {
    if (n % k === 0) {
      n /= k;
      res.push(k);
      k = 2;
      continue;
    } else {
      ++k;
    }
  }

  return res;
};

const solve = () => {
  const N = +inputs[0];
  if (N !== 1) {
    const res = factor(N);
    console.log(res.join('\n'));
  }
}

// solve();