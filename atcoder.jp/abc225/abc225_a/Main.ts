import * as fs from 'fs';

const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("")

let result = 3

if (input[0] === input[1] && input[0] === input[2]) {
  result = 1
} else if (input[0] != input[1] && input[0] != input[2] && input[1] != input[2]) {
  result = 6
}

console.log(result)