#!/usr/bin/node
// script that prints a square
const { argv } = require('process');
try{
	if(isNaN(argv[2])) throw "z";
  for(let i = 0; i < parseInt(argv[2]); i++){
    for(let j = 0; j < parseInt(argv[2]); j++){
      process.stdout.write("X")
    }
    process.stdout.write("\n")    
  }
} catch(err){
  console.log("Missing size")
}