import * as fs from "fs"
const input = fs.readFileSync("/dev/stdin", "utf8").split(/ |\n/g)
const s = input[0].substr(-1);

if (s == "r") console.log("er");
else console.log("ist")