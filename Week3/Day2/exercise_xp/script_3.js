let allBoldItems = getBold_items()

function getBold_items(){
	let bold = document.body.firstElementChild.children
	console.log(bold)		
}


function highlight(){
	allBoldItems.style.color = ("blue")
}

highlight.onmouseover()

function return_normal(){
	allBoldItems.style.color = ("blue")
}

return_normal.onmouseout()






