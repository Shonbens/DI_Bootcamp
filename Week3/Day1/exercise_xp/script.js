//exercise 1

document.getElementById("navBar").id = "socialNetworkNavigation";

let NewLi = document.createElement("li")
let NewText = document.createTextNode("Logout")
NewLi.appendChild(NewText)
socialNetworkNavigation.lastElementChild.appendChild(NewLi)

