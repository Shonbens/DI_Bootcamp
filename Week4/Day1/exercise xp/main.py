#exercise 1:
print("hello world"*4)

#exercise 2:
print(int(99 ** 3) * 8)

#exercise 3:
print(5 < 3) #false
print(3 == 3) #true
print(3=="3") #false
#print("3">3) #cant compare string and int
print("Hello" == "hello") #false

#exercise 4:
computer_brand = "apple"
print("I have a", computer_brand, "computer")

#exercise 5:
name = "shon"
age = int(22)
shoe_size = int(43)
info = ("my name is",name,"i am",age,"and my shoe size is",shoe_size,)
print(info)

#exercise 6:
a = 4
b = 3
if a > b:
    print("hello world")

#exercise 7:
number = int(input("enter a number"))
if (number % 2) == 0:
    print("number is even")
else:
    print("number is odd")

#exercise 8:
user_name = input("what is your name?")
if user_name == "shon":
    print("we have the same name")
else:
    print("i don't like you")

#exercise 9
height = int(input("enter your name in inches"))
if height > 145:
    print("you are tall enough to ride")
else:
    print("you need to grow to ride")