//exercise 1
console.log(document.body.firstElementChild.firstElementChild)

let child = document.body.firstElementChild.lastElementChild
let parent = document.body.firstElementChild
parent.removeChild(child);

let header = document.body.firstElementChild.children[1]
header.onclick = function() {
	header.style.background="red";
}

let third = document.body.firstElementChild.children[2]
console.log(third)

third.onclick = function() {
	third.style.display="none";
}



let btn = document.createElement("button");
btn.textContent = "bold";
document.body.appendChild(btn);

btn.onclick = function() {
	let paragraph = document.getElementsByClassName("myP").bold()

}

	



