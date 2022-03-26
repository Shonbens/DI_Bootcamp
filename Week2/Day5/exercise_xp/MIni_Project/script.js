function playTheGame() {
	let userAnswer = confirm("Do you want to play the game?");
	console.log(userAnswer);

	if(userAnswer === false){
		alert("No problem, Goodbye")
	} 
	else {
		alert("Let's play")

		let userNumber = Number(prompt("Whats your number?"))
			console.log(userNumber);
			if (isNaN(userNumber)) 
			{
				alert("Sorry not a number, Goodbye")
			}
			else if (userNumber < 0 || userNumber > 10) {
				alert("Sorry not a good number, goodbye")
			}
			else {
				let ComputerNumber = Math.floor(Math.random() * 11);
				console.log(ComputerNumber);

				test(userNumber,ComputerNumber)
			}
	}
}

let counter = 0
function test(userNumber,ComputerNumber){
	console.log(counter,userNumber,ComputerNumber);
	if (counter > 3){
		alert("You,loose")
		return
	}
	 if (userNumber === ComputerNumber) {
	 	alert("WINNER")
	 }
	 else if (userNumber > ComputerNumber) {
	 	alert("Your number is bigger than the computer number, try again." );	
	 	prompt("Have another guess!");
	 	counter++
	 }
	 else if (userNumber < ComputerNumber) {
	 	alert("Your number is smaller than the computer number, try again");
	 	prompt("Have another guess!");
	 	counter++

	 }

}