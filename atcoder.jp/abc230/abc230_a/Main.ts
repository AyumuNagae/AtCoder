import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
var n :number = +input[0]
if (n>=42) n++
const a = '00' +String(n)
console.log('AGC' + a.slice(-3))