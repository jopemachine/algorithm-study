const find = (sortedArr, target, start = 0, end = sortedArr.length) => {
  const nextIdx = Math.floor((start + end) / 2);

  if (sortedArr[nextIdx] === target) {
    return nextIdx;
  }

  // 찾고자 하는 값 보다 작음. => 오른쪽을 보자
  if (sortedArr[nextIdx] < target) {
    if (nextIdx === start) return -1;
    return find(sortedArr, target, nextIdx, end);
  }

  // 찾고자 하는 값 보다 큼. => 왼쪽을 보자
  if (sortedArr[nextIdx] > target) {
    if (nextIdx === end) return -1;
    return find(sortedArr, target, start, nextIdx);
  }
}

