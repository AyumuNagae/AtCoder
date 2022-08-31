import * as fs from 'fs';
 
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n')
const [a, b] = input[0].split(' ').map(Number)
const [c, d] = input[1].split(' ').map(Number)
console.log(a*d-b*c)