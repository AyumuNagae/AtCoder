import * as fs from 'fs';
const input = fs.readFileSync("/dev/stdin", "utf8");
const a = +input.split('\n')[0];

if (a%100 === 0 && a != 0) console.log("Yes")
else console.log("No")