// Practice with Strings
var name = prompt("What is your name?"); 
var char1 = name.slice(0,1); 
var remainingChar = name.slice(1,name.len); 
char1 = char1.toUpperCase(); 
remainingChar = remainingChar.toLowerCase(); 
 
alert("Hello " + char1 + remainingChar);
