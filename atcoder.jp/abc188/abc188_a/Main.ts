import * as fs from 'fs';
const input = fs.readFileSync('/dev/stdin', 'utf8');
const [x,y] = input.split(' ').map(Number)
if (Math.abs(x-y) >=3) {
  console.log("No")
} else {
  console.log("Yes")
}