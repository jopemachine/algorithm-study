/*
==============================================================================================
@ Title: 적어도 대부분의 배수
@ URL: https://www.acmicpc.net/problem/1145
@ Created Date: 7/5/2022, 5:20:48 PM
@ Problem:
다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다. 서로 다른
다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 다섯 개의 자연수가 주어진다. 100보다 작거나 같은 자연수이고, 서로 다른 수이다.
@ Output: 첫째 줄에 적어도 대부분의 배수를 출력한다.
==============================================================================================
*/

fn main() {
  let mut input = String::new();
  std::io::stdin().read_line(&mut input).unwrap();
  let mut nums = input.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
  nums.sort();

  let mut res = nums[0];

  loop {
    let mut cnt = 0;
    for i in 0..5 {
      if res % nums[i] == 0 {
        cnt += 1;
      }
    }

    if cnt >= 3 {
      break;
    }

    res += 1;
  }

  println!("{}", res);
}
