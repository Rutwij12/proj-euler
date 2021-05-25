//You are going to write a function which will select a random name from a list of names. The person selected will have to pay for everybody's lunch!

var names = ["Michael", "Pam", "Jim", "Dwight", "Stanley"]; 

function whosPaying(names) {
var namesLength = names.length; 
var randomNo = Math.floor((Math.random() * namesLength)); 

console.log(names[randomNo] + " is going to buy lunch today!"); 
}
