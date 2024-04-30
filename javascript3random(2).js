// 1) Write a javascript function to find the factorial of a number.

function factorized(n){
    if (n===0){
        return 1
    }
    else{
        return n * factorized(n - 1)
    }
}

val= parseInt(prompt('Enter number'))
console.log(`${val} have the factorial answer: ${factorized(val)}`)


// 2) Create a javascript program to count the number of occurrences of each character in a given string.

function counting(word){

    temp_dict={}

    for(let i=0; i <= word.length; i++){
        let char=word[i] //only 1 letter we save in char and we use to check
        if (temp_dict[char]){
            temp_dict[char]++
        }
        else{
            temp_dict[char] = 1
        }
    }

    for (let char in temp_dict) {
        console.log(`'${key}' occurs ${temp_dict[char]} times`);
    }
}

string=prompt('enter word')
counting(string)


// 3)Implement a javascript class representing a simple bank account with methods to deposit, withdraw, and check balance.
class BankAccount{ //this is no round bracket here 
    constructor(balance){
        this.bal=balance
    }

    deposit(amount){ // no function keyword need
        this.bal+=amount
    }

    withdraw(amount){
        this.bal-=amount
    }

    check_bal(){
        return `your bal is ${this.bal}`
    }
}

user1=new BankAccount(5000) //must use new keyword always

user1.deposit(1000)
console.log(user1.check_bal())

user1.withdraw(500)
console.log(user1.check_bal())
