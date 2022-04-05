# exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = zip(keys, values)
print(list(result))

# exercise 3

brand = {
    1: {
        "name": "zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega",
        "type_of_clothes": "men, women, children, home",
        "international_competitors": "Gap, H&M, Benetton",
        "number_stores": 7000,

    },
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    },
}

brand[1]["number_stores"] = 2
print("Zaras clients are mostly young people")
brand["country_creation"] = "spain"
brand[1]["international_competitors"] = "Gap, H&M, Benetton, Desigual"
del brand[1]["creation_date"]
print(brand[1]["international_competitors"][20:28])
print(brand["major_color"]["US"])
print(len(brand))
for key, value in brand.items():
    print(key)

more_on_zara = {
    "details": {
        "creation_date": 1975,
        "number_stores": 10000
    }
}

from collections import ChainMap

d3 = dict(ChainMap(brand, more_on_zara))
print("Merge the dictionaries", d3)

print(d3["details"]["number_stores"])

# exercise 4

from collections import OrderedDict

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {k: v for v, k in enumerate(users)}
print(disney_users_A)

disney_users_B = {index: value for index, value in enumerate(users)}
print(disney_users_B)

ordered = OrderedDict(sorted(disney_users_B.items(), key=lambda t: t[1]))
print(ordered)



