//1) Fibonacci Sequence: Write a javascript function to generate the Fibonacci sequence up to a specified number of terms.
function fib(val){
    let temp=[0,1]

    for(i=2;i<=val;i++){
        temp.push(temp[i-1]+temp[i-2])
    }

    return temp
}
let num=parseInt(prompt('enter numebr'))
console.log(fib(num))


//2) Palindrome Check: Write a javascript function to check if a given string is a palindrome.
function palin(word){
    let clean= word.replace('/[\W_]g/','').toLowerCase()
    let tempArr=[]

    tempArr= clean.split('')
    tempArr=tempArr.reverse()
    reversed=tempArr.join('')

    return clean == reversed ? "it's palindrome" : "It's not palindrome"
}

let word =prompt('enter word')
console.log(word,palin(word))


//3)Prime Number Check: Write a javascript function to determine whether a given number is prime or not.
function prime(n){
    if(n <= 1){
        return 'it is non-prime'
    }
    max=Math.round(Math.sqrt(n,0.5)+1) //math.round - convert float to whole value, math.sqrt(base,exponent) -> give floating value 
    console.log(max)
    for(i=2;i<max;i++){
        if (n % i == 0){
            return "it's not prime number"
        }
    }
    return "it's prime number"
}

num=parseInt(prompt('enter number'))
console.log(prime(num))
