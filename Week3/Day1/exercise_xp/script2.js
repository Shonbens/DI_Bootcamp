//Exercise 2

let FirstList = document.getElementsByClassName("list")[0]
let SecondList = document.getElementsByClassName("list")[1]

FirstList.children[1].textContent = "Richard"

SecondList.children[0].textContent = "Shon"

document.getElementsByClassName("list")[1].children[0].textContent = "Shon"

let NewLi = document.createElement("li")
let NewText = document.createTextNode("Hey students")
NewLi.appendChild(NewText)

let NewLi2 = document.createElement("li")
let NewText2 = document.createTextNode("Hey students")
NewLi2.appendChild(NewText2)


FirstList.lastElementChild.appendChild(NewLi)
SecondList.lastElementChild.appendChild(NewLi2)

SecondList.children[1].textContent = ""







