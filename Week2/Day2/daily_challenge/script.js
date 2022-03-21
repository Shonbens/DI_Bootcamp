let sentence = "The movie is not that bad I like it."
let sentenceArr = sentence.split(" ")
var wordNot = sentenceArr.indexOf("not")
var wordBad = sentenceArr.indexOf("bad")

if ( wordBad > wordNot ) {
	console.log(sentence.replace("not that bad","good,"));

} else {
	console.log(sentence);
}