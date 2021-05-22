//Final Version

function fibonacciGenerator(n) { 
var fibonacciArray = []; 

if (n == 1){
  fibonacciArray.push(0); 
  console.log(fibonacciArray); 
}
else if (n == 2){
    fibonacciArray.push(0, 1);  
   console.log(fibonacciArray); 
}
else{
  
  fibonacciArray.push(0, 1);

  for (var i = 3; i <= n; i++){
  
  var val1 = fibonacciArray[i - 3];
  var val2 = fibonacciArray[i - 2];

  fibonacciArray.push(val1 + val2); 
  }
  console.log(fibonacciArray);
}



}
