# exercise 1
from random import choice


def get_words_from_file(file):
    with open(file, "r") as f:
        list_of_words = f.readlines()
        list_of_words = [word.replace("", "") for word in list_of_words]
        return list_of_words


def get_random_sentence(length):
    global sentenceInAList
    thelist = get_words_from_file("words.txt")
    for i in range(length):
        sentenceInAList = []
        randomWord = choice(thelist).lower()
        sentenceInAList.append(randomWord)
        print(sentenceInAList)
    sentence = (" ".join(sentenceInAList))
    return sentence


def main():
    """asks for a number and joins it in a sentence"""
    choices = int(input("input a number Between 2-20"))
    if 2 <= choices <= 20:
        sentence = get_random_sentence(choices)
        return sentence
    else:
        print("incorrect number")


main()

# exercise 2
import json

sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}

print(sampleJson['company']["employee"]["payable"]["salary"])
sampleJson["company"]["employee"]["birthday"] = "1995-12-30"
print(sampleJson)

with open('exercise.json', 'w') as f:
    json.dump(sampleJson, f)
