const input = require("fs")
    .readFileSync("/dev/stdin", "utf8")
    .trim()
    .split("\n");

const s: string = input[0];
console.log(s[1]+s[2]+s[0]);
