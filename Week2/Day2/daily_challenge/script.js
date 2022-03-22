let sentence = "The movie is not that bad I like it."
let sentenceSplit = sentence.split(" ")
var wordNot = sentenceSplit.indexOf("not")
var wordBad = sentenceSplit.indexOf("bad")

if ( wordBad > wordNot ) {
	console.log(sentence.replace("not that bad","good,"));

} else {
	console.log(sentence);
}