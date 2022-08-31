import * as fs from 'fs';

const lines = fs.readFileSync("/dev/stdin", "utf8").split("\n");
const k:Number = lines[0]
const [a, b] = lines[1].split(' ').map(Number)

const x = Math.floor(a / k);
const y = Math.floor(b / k);
console.log(a % k !== 0 && x === y ? 'NG' : 'OK');