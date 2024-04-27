// 1)revserse string -> write a javascript to reverse a string without any buit in methods like reverse() or slicing
function reversed(strings){
    let reversed=''

    // becuase we want to make reverse you always take high number right then make minus until it reach 0
    for(i=strings.length - 1 ;i >= 0; i--){
        reversed= reversed + strings[i]  //one by one we add character
    }
    return reversed //last we return
}
let word=prompt('enter your word:')
console.log(reversed(word))


// 2)Checking if a string is a palindrome in javascript
function check_palin(string){

    // W i sfor all non-character  \W is same as [^A-za-z0-9] and underscore is _
    //[^A-z] -> ^ is use to neglate anything that in that list
    let clean_word=  string.replace('/[\W_]/g','').toLowerCase()
    let reversed = clean_word.split('').reverse().join('');
    
    return clean_word == reversed
}
let word=prompt('enter your word:')
console.log(word,'is palindrome:' ,check_palin(word))


// 3) Calculating the factorial of a given number using recursion in javascript:
function factor(n){
    if (n==0){
        return true
    }
    else{
        return n * factor(n-1)
    }
}
let num=parseInt(prompt('enter number:'))
console.log(num,'factorized answer:' ,factor(num))
