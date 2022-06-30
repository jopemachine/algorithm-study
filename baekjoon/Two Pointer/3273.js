const readline = require('readline');
const inputs = [];
// const inputs = [
//   '9',
//   '5 12 7 10 9 1 2 3 11',
//   '13'
// ];

readline
  .createInterface(process.stdin, {})
  .on('line', function(line) {
    inputs.push(line.trim());
  }).on('close', function() {
    solve();
  });

const solve = () => {
  const N = +inputs[0];
  const nums = inputs[1].split(' ').map(e => +e);
  const X = +inputs[2];

  nums.sort((a, b) => a - b);

  let left = 0;
  let right = nums.length - 1;

  let cnt = 0;
  while (left < right) {
    const sum = nums[left] + nums[right];

    if (sum === X) {
      ++cnt;
      ++left;
    } else if (sum > X) {
      --right;
    } else {
      ++left;
    }
  }

  console.log(cnt);
};

// solve();