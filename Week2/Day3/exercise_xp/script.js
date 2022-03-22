//exercise 1

let people = ["Greg", "Mary", "Devon", "James"];

//1 
people.shift()
console.log(people)

//2
people.pop()
console.log(people)
people.push("jason")
console.log(people)

//3
people.push("Shon")
console.log(people)

//4
console.log(people.indexOf("Mary"))

//5
console.log(people.slice(1))

//6
//console.log(people.indexOf("foo")) //foo is a placeholder. It returns -1 because it saves that place.

//7
let last = people[3]
console.log(last)

//Part II - Loops

//1
for (let names of people){
	console.log(names)
}

//2

for (let i = 0; i < people.length; i++) {
	if (i === 3) {
		break;
	}
	console.log(people[i]);
}



//exercise 2

let colors = ["black","red","yellow","white","blue"]
let choice = ["#1 ","#2 ","#3 ","#4 ","#5 "]

for (let i = 0; i < colors.length; i++)
	for (let i2 = 0; i2 < choice.length; i2++)
	 {
	console.log(`My ${choice[i]}choice is ${colors[i]}`);
}

//exercise 3

//1
let number = prompt("Enter a number");

//2
if (number < 10) {
	//let number = prompt("Enter a number");
}

//exercise 4

//1

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

//2
console.log(building["numberOfFloors"])

//3
console.log(building["numberOfAptByFloor"]["firstFloor"])
console.log(building["numberOfAptByFloor"]["thirdFloor"])

//4
console.log(building["nameOfTenants"][1])
console.log(building["numberOfRoomsAndRent"]["dan"][0])

//5
let sum = (building["numberOfRoomsAndRent"]["sarah"][1]) +
(building["numberOfRoomsAndRent"]["david"][1])

console.log(sum)

console.log(building["numberOfRoomsAndRent"]["dan"][1] + 200)

//exercise 5 

let family = {
	dad: "jason",
	mom: "emily"
}

console.log(Object.keys(family));
console.log(Object.values(family))



//exercise 6 

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

console.log("my " + details["my"] + " is " +  details["is"]+ " the " + details["the"])

//exercise 7 

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

console.log((names[3][0]),(names[4][0]),(names[0][0]),(names[5][0])
	,(names[1][0]),(names[2][0]))


