import * as fs from "fs"
 
const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
const a :number = +input[0]
const b :number = +input[1]

if (a>=b) console.log(0);
else console.log(Math.ceil( (b-a)/10  ))