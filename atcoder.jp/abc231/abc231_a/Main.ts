import * as fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
const a :number = +input[0]

console.log(a/100)