#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) return (0);
  else if (n === 0) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(Number(process.argv[2])));
