#!/usr/bin/node
// script that prints a square
const { argv } = require('process');
const isvalid = () => {
  if(argv[2]  === undefined) return false;
  let i = 0;
  for(const x of argv[2]){
    if(x=== '-' && i === 0) {i++; continue;}
    
    if(isNaN(x)) return false;
  }
  return true;
}
if(isvalid()){
  const size = parseInt(argv[2]);
  let output = '';
  for (let x = 0; x < size; x++) {
    output = output.concat('x');
  }
  for (let y = 0; y < size; y++) {
    console.log(output);
  }
}
else{
  console.log("Missing size")
}