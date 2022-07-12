import * as fs from 'fs';
const input = fs.readFileSync("/dev/stdin", "utf8");

const a = "000" + input

console.log(a.slice(-5))