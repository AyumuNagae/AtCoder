import * as fs from "fs"

const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
const s :string = input[0]
const a :number[] = s.split("").map((s: string) => Number(s))
console.log(  (a[0]+a[1]+a[2])*111 )