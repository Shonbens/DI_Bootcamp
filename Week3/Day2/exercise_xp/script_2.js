//Exercise 2
//let form = document.body.firstElementChild
//console.log(form)

let idF = document.getElementById("fname")
console.log(idF)
let idL = document.getElementById("lname")
console.log(idL)
let idS = document.getElementById("submit")
console.log(idS)


//let firstInput = formElements[0];
//let secondInput = formElements[1];

let formDetail = document.forms[0]
let formElements = formDetail.elements;
console.log(formElements)

function retrieveFormInfo (evt) {
	evt.preventDefault();
	let firstInput = evt.target.elements[0].value;
	let secondInput = evt.target.elements[1].value;
	let paragraph = document.getElementsByClassName("usersAnswer");
	paragraph.textContent += `The data is ${firstInput} and ${secondInput}`; 
}

formDetail.addEventListener("submit", retrieveFormInfo)












