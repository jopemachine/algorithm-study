/*
==============================================================================================
@ Title: 약속
@ URL: https://www.acmicpc.net/problem/1183
@ Created Date: 7/5/2022, 11:24:13 AM
@ Problem:
마법사 N명이 머글 문화를 이해하기 위해 머글과 약속을 잡았다. 각 마법사는 한 명의 머글을 만날 예정이다. 하지만, 마법사는 약속
시간보다 빨리 또는 늦게 도착할 수 있기 때문에 고민에 빠졌다. 결국 기다리는 시간을 최소화 하기 위해 모든 약속 시간을 T씩 미루려고
한다. 기다리는 시간은 먼저 도착한 사람이 늦게 도착한 사람이 도착할 때까지 기다리는 시간을 의미한다. 마법사의 약속 시간은 A1,
A2, ..., AN이고, 도착 시간은 B1, B2, ..., BN이다. 약속 시간을 T만큼 미루면, 기다리는 시간의 합은 |Ai +
T - Bi|의 합과 같다. 기다리는 시간의 합이 최소가 되는 서로 다른 정수 T의 개수를 구해보자.
@ Input: 첫째 줄에 N이 주어진다. 다음 N개의 줄에 Ai, Bi가 주어진다.
@ Output: 첫째 줄에 기다리는 시간의 합이 최소인 서로 다른 정수 T의 개수를 출력한다.
==============================================================================================
*/

use std::io;

fn main() {
  let mut input = String::new();
  std::io::stdin().read_line(&mut input).unwrap();
  let mut tokens = input.split_ascii_whitespace();
  let N = tokens.next().unwrap().parse::<u32>().unwrap();
  
  if N % 2 == 1 {
    println!("{}", 1);
    return;
  }

  let mut diffs: Vec<i32> = Vec::with_capacity(N as usize);

  for _i in 0..N {
    let mut input = String::new();
    let tokens;

    std::io::stdin().read_line(&mut input).unwrap();
    tokens = input.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    if let [a, b] = tokens[..] {
      diffs.push(a - b);
    } else {
      panic!("something wrong!");
    }
  }

  diffs.sort();

  let median1 = diffs[(N / 2) as usize];
  let median2 = diffs[((N - 1) / 2) as usize];

  println!("{}", median1 - median2 + 1);
}