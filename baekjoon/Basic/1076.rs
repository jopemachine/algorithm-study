/*
==============================================================================================
@ Title: 저항
@ URL: https://www.acmicpc.net/problem/1076
@ Created Date: 7/4/2022, 9:35:04 PM
@ Problem:
전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은
곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다. 색 값 곱 black 0 1 brown 1 10 red 2 100
orange 3 1,000 yellow 4 10,000 green 5 100,000 blue 6 1,000,000 violet 7
10,000,000 grey 8 100,000,000 white 9 1,000,000,000 예를 들어, 저항의 색이 yellow,
violet, red였다면 저항의 값은 4,700이 된다.
@ Input Example: 첫째 줄에 첫 번째 색, 둘째 줄에 두 번째 색, 셋째 줄에 세 번째 색이 주어진다. 위의 표에 있는 색만 입력으로 주어진다.
@ Output Example: 입력으로 주어진 저항의 저항값을 계산하여 첫째 줄에 출력한다.
==============================================================================================
*/

use std::io;
use std::collections::HashMap;

fn main() {
  let valueDict = HashMap::from([
    ("black",  "0"),
    ("brown",  "1"),
    ("red",    "2"),
    ("orange", "3"),
    ("yellow", "4"),
    ("green",  "5"),
    ("blue",   "6"),
    ("violet", "7"),
    ("grey",   "8"),
    ("white",  "9"),
  ]);

  let multipleValueDict = HashMap::from([
    ("black",  1),
    ("brown",  10),
    ("red",    100),
    ("orange", 1000),
    ("yellow", 10000),
    ("green",  100000),
    ("blue",   1000000),
    ("violet", 10000000),
    ("grey",   100000000),
    ("white",  1000000000),
  ]);

  let mut color1 = String::new();
  let mut color2 = String::new();
  let mut color3 = String::new();

  std::io::stdin().read_line(&mut color1).unwrap();
  std::io::stdin().read_line(&mut color2).unwrap();
  std::io::stdin().read_line(&mut color3).unwrap();

  let mut result = (format!("{}{}", valueDict[&color1.trim()[..]], valueDict[&color2.trim()[..]])).parse::<i64>().unwrap();
  let multiple: i64 = multipleValueDict[&color3.trim()[..]];
  println!("{}", result * multiple);
}
