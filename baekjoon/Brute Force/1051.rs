/*
==============================================================================================
@ Title: 숫자 정사각형
@ URL: https://www.acmicpc.net/problem/1051
@ Created Date: 7/4/2022, 9:02:12 PM
@ Problem:
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰
정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.
@ Input Example: 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.
@ Output Example: 첫째 줄에 정답 정사각형의 크기를 출력한다.
==============================================================================================
*/

use std::io;
use std::cmp;

fn main() {
  let mut str = String::new();
  std::io::stdin().read_line(&mut str).unwrap();
  let mut tokens = str.split_ascii_whitespace();
  let N: u32 = tokens.next().unwrap().parse::<u32>().unwrap();
  let M: u32 = tokens.next().unwrap().parse::<u32>().unwrap();

  let mut map = Vec::new();

  for i in 0..N {
    let mut tmp = String::new();
    std::io::stdin().read_line(&mut tmp).unwrap();
    map.push(tmp.clone());
  }

  let mut result = 1;

  for i in 0..N as usize {
    for j in 0..M as usize {
      for k in 0..cmp::min(N, M) as usize {
        if i + k >= N as usize || j + k >= M as usize {
          continue;
        }

        let p1 = map[i].chars().nth(j).unwrap();
        let p2 = map[i].chars().nth(j + k).unwrap();
        let p3 = map[i + k].chars().nth(j).unwrap();
        let p4 = map[i + k].chars().nth(j + k).unwrap();

        if p1 == p2 && p2 == p3 && p3 == p4 {
          let area = (k + 1) * (k + 1);
          result = cmp::max(result, area);
        }
      }
    }
  }

  println!("{}", result);
}
