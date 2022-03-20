//exercise 1

let favoriteFood = "Hamburguer";

let favoriteMeal = "Dinner";

let sentence = `I eat ${favoriteFood} at every ${favoriteMeal}`
console.log(sentence)

//exercise 2

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

let myWatchedSeriesLength = 3

let myWatchedSeriesSentence = `I watched ${myWatchedSeriesLength} series: ${myWatchedSeries}`
console.log(myWatchedSeriesSentence)

//part II

myWatchedSeries.splice(2,1,"friends","vikings")

myWatchedSeries.splice(0,1,"narcos")

let moneyHeist = "money heist"
console.log(moneyHeist.substring(2,3))

console.log(myWatchedSeries)

//exercise 3

let temperatureC = "3°C"

let temperatureF = "37°F."

let temperatureSentence = `${temperatureC} is ${temperatureF}`
console.log(temperatureSentence)

//exercise 4

let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:It will output 55 because they are numbers.
    // Actual: 55

    a = 2;

    console.log(a+b) //second expression
    // Prediction: It will output 23 because they changed the value of a to 2.
    // Actual: 23

    //3. The value of c is 3421

    console.log(3 + 4 + '5');
    //the outcome will be 75 because you add the first 2 numbers and then ad the to the string.

    //exercise 5

typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction: number
// Actual: number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:boolean
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction: It will add an s at the end of the sentence
// Actual: added an s

"hamburgers" - "s"
// Prediction: Nan because you cant substract strings
// Actual: Nan

"1" + "3"
// Prediction: 13
// Actual: 13

"1" - "3"
// Prediction:-2
// Actual:-2

"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:nan
// Actual:nan

99 * "hello"
// Prediction:nan
// Actual:nan

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false

//exercise 6


5 + "34"
// Prediction:534
// Actual:534

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction: 0
// Actual: 0

5 % 10
// Prediction: 5
// Actual: 5

"Java" + "Script"
// Prediction: JavaScript
// Actual: JavaScript

" " + " "
// Prediction: nothing
// Actual: nothing

" " + 0
// Prediction: 0
// Actual: 0

true + true
// Prediction: 2
// Actual: 2

true + false
// Prediction: 1
// Actual: 1

false + true
// Prediction: 1
// Actual: 1

false - true
// Prediction:-1
// Actual:-1

!true
// Prediction:false
// Actual:false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction:Nan
// Actual:Nan






