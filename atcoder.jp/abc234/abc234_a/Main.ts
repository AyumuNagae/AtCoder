import * as fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
const t :number = +input[0]

function f(t:number):number {
  return t**2 + t*2 + 3
}

console.log(   f(f(f(t)+t)+f(f(t)))     )