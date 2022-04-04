#exercise 1

my_fav_numbers={1,2,3}
more_numbers=[4,5]
my_fav_numbers.update(more_numbers)
print(my_fav_numbers)
my_fav_numbers.remove(5)
print(my_fav_numbers)
friend_fav_numbers={6,7,8}
my_fav_numbers.update(friend_fav_numbers)
our_fav_numbers=my_fav_numbers
print(our_fav_numbers)

#exercise 2
#No, it is not possible, they are immutable.

#exercise 3
for i in range(0,21):
    print(i)

#exercise 4
#1 A float is a decimal, an integer is a whole number.

from itertools import islice, count

def iter_range(start, stop, step):
    if step == 0:
        raise ValueError("Step could not be NULL")
    length = int(abs(stop - start) / step)
    return islice(count(start, step), length)

for it in iter_range(1.5, 5.5, 0.5):
    print("{0:.1f}".format(it), end = " ")
    print()


#exercise 5

basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket=["Apples"]+basket
count = basket.count("Apples")
print(count)
print(basket)
print(basket.clear())

#exercise 6

#while True:
   # name=input("What is your name?")
   # if name == "shon":
        #print("good job")
       # break
  #  else:
       # print("try again")

#exercise 7

num = [0,1,2,3,4,5,6]
print("The original list: " + str(num))
res = num[::2] + num[1::2]
print("even nums: " + str(res))

#exercise 8

for x in range(1500,2501):
    if x % 7 == 0:
        print(x)


#exercise 9

#user_fruits = input("what is your fav fruit? separate them with a space")
#split = user_fruits.split(" ")
#print(split)
#select_fruit = input("Name any fruit:")

#if select_fruit == user_fruits:
   # print("You chose one of ur fav fruits! enjoy!")
#else:
    #print("You chose a new fruit")

#exercise 10

choice = ""

while choice != "exit":
    choice = input("olives,mushrooms, pineapple? type exit to stop.")
    if choice == 'olives':
        print("I will ad it")
    elif choice == 'mushrooms':
        print("i will ad it")
    elif choice == 'pineapple':
        print("i will add it")
    else:
        print("That is not a valid input.")

#exercise 11

question = int(input("Enter age"))
if question < 3:
    print("ticket is free")
elif question > 3 < 12:
    print("the ticket is $10")
else:
    print("the ticket is $15")

#exercise 12
enter_name = (input("What is your name"))
age = int(input("Enter age"))
if age < 16:
   enter_name.remove()

#exercise 13
print("the deli has run out of pastrami!")
sandwich_orders=["cheese","beef","salami","pastrami","pastrami",
                 "pastrami"]
finished_sandwiches = (sandwich_orders)
print(finished_sandwiches)

#exercise 14

finished_sandwiches = list(filter(("pastrami").__ne__, finished_sandwiches))
print(finished_sandwiches)






















































