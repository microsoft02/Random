//1) Write a javascript function to check if a string is a palindrome.
function palindrome(word){
    clean_word =  word.replace('/[\W_]g/','').toLowerCase()

    reversed_Word=''
    for (char in clean_word){
        reversed_Word = char + reversed_Word
    }
    return reversed_Word == clean_word ? 'it is palindrome': 'it is not palindrome'
}

string=prompt('enter the word')
console.log(`${string} ${palindrome(string)}`)


//2) Implement a javascript function to calculate the factorial of a given number recursively.
function factorial_check(n){
    if(n == 0){
        return 1
    }
    else{
        return n * factorial_check ( n - 1)
    }
}

num=parseInt(prompt('enter number'))
console.log(num +'factorial answer:' + factorial_check(num))


//3) Create a javascript program to find the largest and smallest elements in a list.
function finder(temp){

    // must use sort method
    temp.sort((a,b) => a - b);

    //we return object key and value pair
    return {'lowest': temp[0], 'highest': temp[temp.length - 1]}
}

temp_list=[4,3,1,5,2]
let result = finder(temp_list)

//accessing key that is in result
console.log('lowest:'+ result.lowest +' highest:' + result.highest)
