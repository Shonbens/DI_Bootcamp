let planets = ["mars","jupiter","earth","venus","mercury","pluto","saturn","uranus"]

for (let i=0; i<planets.length; i++) {

	let newPlanet = document.createElement("div");
	newPlanet.classList.add("planet");
	newPlanet.style.background = planets[i];
	document.querySelector(".listPlanets").appendChild(newPlanet);
}