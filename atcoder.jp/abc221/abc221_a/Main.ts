import * as fs from 'fs';
const arg = fs.readFileSync("/dev/stdin", "utf8")
const input = arg.trim().split("\n").filter(e => { return e !== '' })

const [A,B] = input[0].split(" ").map((s:string) => Number(s))
console.log(32**(A-B))