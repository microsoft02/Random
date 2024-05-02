//1)Write a javascript function to check if a given string is a palindrome or not.
function check_palin(string){
     let cleaned=  string.replace('/[\W_]/g','').toLowerCase()
     let reversed = clean_word.split('').reverse().join('');
    
     return cleaned === reversed
}

let word=prompt('enter your word:')
console.log(word,'is palindrome:' ,check_palin(word))


// 2) Create a javascript program to find the factorial of a number using recursion.
function fact_check(n){
    if(n == 0){
        return 1
    }
    else{
        return n * factorial_check ( n - 1)
    }
}
    
value=parseInt(prompt('enter number'))
console.log(value +'factorial answer:' + fact_check(num))


// 3)Implement a javascript class representing a simple bank account with methods to deposit, withdraw, and check balance.
class bank_account{
  constructor(bal){
       this.bal=bal
  }

  deposit(amount){
      this.bal+=amount
  }

  withdraw(amount){
      this.bal-=amount
  }

  bal(){
      return `your bal is ${this.bal}`
  }
}

person1=new bank_account(3000)

person1.deposit(1000)
console.log(person1.bal())

person1.withdraw(500)
console.log(person1.bal())
