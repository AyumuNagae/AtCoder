import * as fs from 'fs';
const input = fs.readFileSync("/dev/stdin", "utf8")

console.log(Number(input[0]) * Number(input[2]))