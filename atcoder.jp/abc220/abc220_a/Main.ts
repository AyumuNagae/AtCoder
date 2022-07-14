import * as fs from 'fs';
const arg = fs.readFileSync("/dev/stdin", "utf8")
const input = arg.trim().split("\n").filter(e => { return e !== '' })

const [A,B,C] = input[0].split(" ").map((s:string) => Number(s))
let i = 1
let flag = false
while(C*i <= B) {
    if(C*i <= B && A <= C*i){
        flag = true
        break
    }
    i++
}
console.log(flag?C*i:-1)