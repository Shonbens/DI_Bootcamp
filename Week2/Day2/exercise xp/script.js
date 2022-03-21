//exercise 1

let x = 5;
let y = 2;

if(x > y) {
	console.log(`${x} is the biggest number`);
} else {
	console.log(`${y} is the biggest number`);
}

//exercise 2

let newDog = "chihuahua"
console.log(newDog.length)
console.log(newDog.toLowerCase())
console.log(newDog.toUpperCase())

if (newDog === "chihuahua") {
	console.log(`I love ${newDog}, its my favorite dog breed`);
} else {
	console.log(`I dont care, i prefer cats`);
}

//exercise 3 

let number = 5

if (number % 2 == 0) {
	console.log(`${number} is an even number`);
} else {
	console.log(`${number} is an odd number`);
}

//exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users < 1) {
	console.log("no one is online");
} else if (users.length == 1) {
	console.log(`${users} is online`);
} else if (users.length == 2) {
	console.log(`${users} are online`);
} else {
	console.log(`${users.splice(0,2)} and ${users.length} are online`);
}	



