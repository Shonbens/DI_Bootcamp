let sentance = prompt("write a sentence ")
starWord(sentance);

function starWord(array) {
    let sentToArr = array.split(" "); // convert the sentence we recived from the user to an array.

    let bigWord = biggerWord(sentToArr); // reciving the  length of the longet word, which determent the size of the frame.
    let sign = "*";

    let frame = sign.repeat(bigWord + 4) // creating the frame.

    console.log(`${frame}`); //console log the frame.
    for (let j = 0; j < sentToArr.length; j++) {
        let empty = " ";
        let currWord = sentToArr[j];                          
        let space = bigWord - currWord.length;
        console.log(`* ${currWord} ${empty.repeat(space)}*`);
    }

    console.log(`${frame}`);

}

function biggerWord(array) {
    // let sentToArr = array.split(" "); // convert the sentence form the user to an array.
console.log(array);
    let bigWord = 0;
    for (let i = 0; i < array.length; i++) {
        let currWord = array[i];
        let bigCurr = currWord.length;
        if (bigCurr > bigWord) {
            bigWord = bigCurr
        }

    }
    return bigWord;
}