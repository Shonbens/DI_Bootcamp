//exercise1

function infoAboutMe() {
	console.log("I am 22")
}

infoAboutMe()

//part II

function infoAboutPerson (personName, PersonAge, perfonFavoriteColor) {
	console.log(`Your name is ${personName}, you are ${PersonAge}, your favorite color is ${perfonFavoriteColor}`)

}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

//exercise2

function calculateTip() {
	let answer = Number(prompt("What is the bill"));
	if (answer < 50) {
		console.log(answer*0.20+answer)
	} else if (answer <= 200) {
		console.log(answer*0.15+answer)
	} else {
		console.log(answer*0.10+answer)
	}
}

//calculateTip()

//exercise3

function isDivisible() {
	for (let i = 0; i < 500; i+=23){
        console.log(i)
    }     
}
	
isDivisible()

//exercise4

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana","orange","apple"]

function myBill () {
	if (shoppingList = "banana" && stock["banana"]>0) {
		(prices["banana"])
	 } if (true) {
	 	(stock["banana"]-1)
	 }
	 else {
		console.log("banana is out of stock")
	}
	if (shoppingList = "orange" && stock["orange"]>0) {
		console.log(prices["orange"]+prices["banana"])
	 } if (true) {
	 	(stock["orange"]-1)
	 }
	 else {
		console.log("Orange is out of stock")
	}
	if (shoppingList = "apple" && stock["apple"]>0) {
		console.log(prices["apple"]+prices["banana"]+prices["orange"])
	 } if (true) {
	 	(stock["apple"]-1)
	 }
	  else {
		console.log("Apple is out of stock")
	}


}

myBill()

//exercise 6

function hotelCost () {
	let answer = Number(prompt("Number of nights"));
	if(answer == 0){
		let answer = Number(prompt("Number of nights"));
	} else
	console.log(answer*140)
}

//hotelCost()

function planeRideCost () {
	let destination = (prompt("Destination?"));
	if (destination == 0) {
		let destination = (prompt("Destination?"));
	} else if (destination = ("London")) {
		console.log(183)	
	} else if (destination = ("Paris")) {
		console.log(220)	
	} else {
		console.log(300)	
	}
}

//planeRideCost()

function rentalCarCost () {
	let car = Number(prompt("How many days?"));
	if (car == 0 || NaN) {
		let car = Number(prompt("How many days?"))
	} else if (car > 10){
		console.log(car*40-0.05)
	} else {
		console.log(car*40)
	}

}

//rentalCarCost()

function hotelCost () {
	let numberNights;
	
	do {
	 numberNights = +prompt("How many nights will you stay");
}
	while(isNaN(numberNights) || numberNights < 0);

	let PriceForTotalNights = 140*numberNights;
	return PriceForTotalNights;
}


function planeRideCost () {
	let destination=prompt("What is your destination?")

	//if (destination === "" || !isNaN(typeof(Number(destination))) {
		//do {
			//destination=+prompt("What is your destination?")
		//} while(!isNaN)

	//}

	let priceDestination;

	switch(destination) {
		case "London":
			priceDestination = 183;
		break;
		case "Paris":
			priceDestination = 220;
		break;
		default :
			priceDestination = 300;

	}
	return priceDestination
	
}

function rentalCarCost () {
	let numerDays = 2;
	let costCar = numberDays*40

	if (numberDays >= 10) {
		costCar -= costCar*0.05;
	}
	return costCar
}


function totalVacationCost () {
	let costHotel = hotelCost ();
	let costPlane = planeRideCost();
	let costCar = rentalCarCost()
	console.log(`The hotel costs ${costHotel} The Plane cost ${costPlane} The car costs ${costCar}`)

	let total = carcost + costPlane + costHotel
}

totalVacationCost()





